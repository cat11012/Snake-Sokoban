from PIL import Image
import os

def is_red_pixel(r, g, b, threshold=50):
    """Check if pixel is predominantly red"""
    return r > g + threshold and r > b + threshold

def is_green_pixel(r, g, b, threshold=50):
    """Check if pixel is predominantly green"""
    return g > r + threshold and g > b + threshold

def get_distance_from_center(x, y, center_x, center_y):
    """Calculate distance from center point"""
    return ((x - center_x) ** 2 + (y - center_y) ** 2) ** 0.5

def get_color_rgb(color_name):
    """Map color names to RGB values"""
    color_map = {
        'blue': (0, 100, 255),
        'bright_dark_blue': (0, 50, 150),
        'bright_green_blue': (0, 200, 150),
        'bright_green': (0, 255, 100),
        'bright_light_blue': (100, 200, 255),
        'bright_orange': (255, 150, 0),
        'bright_pink': (255, 100, 200),
        'bright_red': (255, 50, 50),
        'bright_yellow': (255, 255, 0),
        'dark_blue': (0, 0, 150),
        'dark_green': (0, 150, 0),
        'dark_orange': (200, 100, 0),
        'dark_red': (150, 0, 0),
        'dark_yellow': (150, 150, 0),
        'green': (0, 255, 0),
        'purple': (150, 0, 255)
    }
    return color_map.get(color_name, (0, 255, 0))  # Default to green

def analyze_image_colors(image_path):
    """Analyze the original image to understand its color structure"""
    img = Image.open(image_path)
    
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    width, height = img.size
    colors = set()
    
    # Collect all unique colors
    for x in range(width):
        for y in range(height):
            r, g, b, a = img.getpixel((x, y))
            if a > 0:  # Skip transparent
                colors.add((r, g, b))
    
    print(f"Original image colors: {sorted(colors)}")
    return sorted(colors)

def analyze_checkpoint_colors(checkpoint_path):
    """Analyze checkpoint file to determine outer (a) and middle (b) colors"""
    img = Image.open(checkpoint_path)
    
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    width, height = img.size
    center_x, center_y = width // 2, height // 2
    color_counts = {}
    
    # Collect all colors and their frequency
    for x in range(width):
        for y in range(height):
            r, g, b, a = img.getpixel((x, y))
            if a > 0:  # Skip transparent
                color = (r, g, b)
                color_counts[color] = color_counts.get(color, 0) + 1
    
    # Sort by frequency (most common first)
    sorted_by_frequency = sorted(color_counts.items(), key=lambda x: x[1], reverse=True)
    colors_only = [color for color, count in sorted_by_frequency]
    
    print(f"Checkpoint colors by frequency: {colors_only}")
    print(f"Color frequencies: {dict(sorted_by_frequency)}")
    
    # Skip black (0,0,0) if it exists, as it's likely background
    non_black_colors = [c for c in colors_only if c != (0, 0, 0)]
    
    if len(non_black_colors) >= 2:
        # First non-black color = outer (a), second = middle (b)
        outer_color = non_black_colors[0]  # Most frequent non-black
        middle_color = non_black_colors[1]  # Second most frequent non-black
    elif len(non_black_colors) == 1:
        outer_color = non_black_colors[0]
        middle_color = non_black_colors[0]  # Same color for both
    else:
        # Fallback - use all colors including black
        outer_color = colors_only[0] if colors_only else (255, 0, 0)
        middle_color = colors_only[1] if len(colors_only) > 1 else outer_color
    
    print(f"Selected outer color (a): {outer_color}")
    print(f"Selected middle color (b): {middle_color}")
    return outer_color, middle_color

def apply_portal_color_pattern(image_path, output_path, color_name):
    """Apply checkpoint colors to portal: preserve exact design, map black to 'a', white to 'b'"""
    
    # First, analyze a checkpoint file to get the color pattern
    checkpoint_path = os.path.join(os.path.dirname(image_path), "..", "checkpoint", "end_point", f"{color_name}_end_point.png")
    
    if os.path.exists(checkpoint_path):
        outer_color_a, middle_color_b = analyze_checkpoint_colors(checkpoint_path)
    else:
        print(f"Checkpoint file not found: {checkpoint_path}")
        # Use default mapping
        outer_color_a = (0, 0, 0)  # Black
        middle_color_b = (255, 255, 255)  # White
    
    # Open the portal image
    img = Image.open(image_path)
    
    # Convert to RGBA mode
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    # Create a copy to modify
    modified_img = img.copy()
    
    # Get image dimensions
    width, height = img.size
    
    # Process each pixel
    for x in range(width):
        for y in range(height):
            r, g, b, a = img.getpixel((x, y))
            
            # Skip transparent pixels
            if a == 0:
                continue
            
            # Map portal colors to checkpoint pattern:
            # Original black pixels -> checkpoint outer color ('a')
            # Original white pixels -> checkpoint middle color ('b')
            
            if (r, g, b) == (0, 0, 0):  # Portal black -> checkpoint outer (a)
                new_color = (outer_color_a[0], outer_color_a[1], outer_color_a[2], a)
            elif (r, g, b) == (255, 255, 255):  # Portal white -> checkpoint middle (b)
                new_color = (middle_color_b[0], middle_color_b[1], middle_color_b[2], a)
            else:
                # Keep any other colors unchanged
                new_color = (r, g, b, a)
            
            modified_img.putpixel((x, y), new_color)
    
    # Save the modified image
    modified_img.save(output_path)

def process_image(image_path, output_path):
    """Process image to change non-red/non-green pixels to green"""
    
    # Open the image
    img = Image.open(image_path)
    
    # Convert to RGBA mode to handle transparency if present
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    # Get image dimensions
    width, height = img.size
    
    # Create a copy to modify
    modified_img = img.copy()
    
    pixels_changed = 0
    total_pixels = width * height
    
    print(f"Processing image: {image_path}")
    print(f"Image dimensions: {width}x{height}")
    print(f"Total pixels: {total_pixels}")
    
    # Process each pixel
    for x in range(width):
        for y in range(height):
            r, g, b, a = img.getpixel((x, y))
            
            # Check if pixel is red or green
            if not (is_red_pixel(r, g, b) or is_green_pixel(r, g, b)):
                # Change to green, keep original alpha
                modified_img.putpixel((x, y), (0, 255, 0, a))
                pixels_changed += 1
    
    print(f"Changed {pixels_changed} pixels to green ({pixels_changed/total_pixels*100:.2f}%)")
    
    # Save the modified image
    # Convert back to original mode if it wasn't RGBA
    if img.mode != 'RGBA':
        modified_img = modified_img.convert(img.mode)
    
    modified_img.save(output_path)
    print(f"Saved modified image to: {output_path}")

def main():
    # Define paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Portal input path
    portal_input_path = os.path.join(script_dir, "portal", "non-color_portal.png")
    
    # Check if portal file exists
    if not os.path.exists(portal_input_path):
        print(f"Error: Portal file not found: {portal_input_path}")
        return
    
    # List of colors based on checkpoint/end_point files
    color_variants = [
        'blue', 'bright_dark_blue', 'bright_green_blue', 'bright_green',
        'bright_light_blue', 'bright_orange', 'bright_pink', 'bright_red',
        'bright_yellow', 'dark_blue', 'dark_green', 'dark_orange',
        'dark_red', 'dark_yellow', 'green', 'purple'
    ]
    
    print("Generating colored portals using actual checkpoint colors:")
    print("  - Portal black pixels -> Checkpoint outer color ('a')")
    print("  - Portal white pixels -> Checkpoint middle color ('b')")
    print("  - Ignoring inner color ('c')")
    print()
    
    success_count = 0
    
    # Generate portal for each color variant
    for color in color_variants:
        try:
            # Define output path
            portal_output_path = os.path.join(script_dir, "portal", f"{color}_portal.png")
            
            # Apply color pattern using checkpoint colors
            apply_portal_color_pattern(portal_input_path, portal_output_path, color)
            
            print(f"✓ Created {color}_portal.png using {color}_end_point.png pattern")
            success_count += 1
            
        except Exception as e:
            print(f"✗ Error creating {color}_portal.png: {e}")
    
    print(f"\nCompleted! Generated {success_count}/{len(color_variants)} portal variants.")
    print("All portals use actual checkpoint color patterns (a=outer, b=middle).")

if __name__ == "__main__":
    main()