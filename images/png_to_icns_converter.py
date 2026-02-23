#!/usr/bin/env python3
"""
PNG to ICNS Converter  
Converts PNG icon files to macOS ICNS format
"""

import os
from PIL import Image

def convert_png_to_icns():
    """Convert all PNG files in icons folder to ICNS format in icons/macOS folder"""
    
    # Define paths
    project_root = os.path.dirname(os.path.dirname(__file__))  # Go up one level from images/
    icons_dir = os.path.join(project_root, 'icons')
    macos_dir = os.path.join(icons_dir, 'macOS')
    
    print(f"Icons directory: {icons_dir}")
    print(f"macOS directory: {macos_dir}")
    
    # Ensure macOS directory exists
    os.makedirs(macos_dir, exist_ok=True)
    
    # Get all PNG files from icons directory
    png_files = [f for f in os.listdir(icons_dir) if f.endswith('.png')]
    png_files.sort()  # Sort for consistent processing
    
    print(f"Found {len(png_files)} PNG files to convert:")
    for png_file in png_files:
        print(f"  - {png_file}")
    
    # Convert each PNG to ICNS
    converted_count = 0
    for png_file in png_files:
        try:
            # Open PNG file
            png_path = os.path.join(icons_dir, png_file)
            with Image.open(png_path) as img:
                # Convert to RGBA if not already (ICNS supports transparency)
                if img.mode != 'RGBA':
                    img = img.convert('RGBA')
                
                # Generate ICNS filename
                icns_name = png_file.replace('.png', '.icns')
                icns_path = os.path.join(macos_dir, icns_name)
                
                # Save as ICNS
                img.save(icns_path, format='ICNS')
                print(f"✓ Converted: {png_file} → {icns_name}")
                converted_count += 1
                
        except Exception as e:
            print(f"✗ Error converting {png_file}: {e}")
    
    print(f"\nConversion complete! {converted_count}/{len(png_files)} files converted successfully.")
    print(f"ICNS files saved to: {macos_dir}")

if __name__ == "__main__":
    convert_png_to_icns()