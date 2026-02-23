#!/usr/bin/env python3
"""
PNG to ICO Converter
Converts PNG icon files to Windows ICO format
"""

import os
from PIL import Image

def convert_png_to_ico():
    """Convert all PNG files in icons folder to ICO format in icons/windows folder"""
    
    # Define paths
    project_root = os.path.dirname(os.path.dirname(__file__))  # Go up one level from images/
    icons_dir = os.path.join(project_root, 'icons')
    windows_dir = os.path.join(icons_dir, 'windows')
    
    print(f"Icons directory: {icons_dir}")
    print(f"Windows directory: {windows_dir}")
    
    # Ensure windows directory exists
    os.makedirs(windows_dir, exist_ok=True)
    
    # Get all PNG files from icons directory
    png_files = [f for f in os.listdir(icons_dir) if f.endswith('.png')]
    png_files.sort()  # Sort for consistent processing
    
    print(f"Found {len(png_files)} PNG files to convert:")
    for png_file in png_files:
        print(f"  - {png_file}")
    
    # Convert each PNG to ICO
    converted_count = 0
    for png_file in png_files:
        try:
            # Open PNG file
            png_path = os.path.join(icons_dir, png_file)
            with Image.open(png_path) as img:
                # Convert to RGBA if not already (ICO supports transparency)
                if img.mode != 'RGBA':
                    img = img.convert('RGBA')
                
                # Generate ICO filename
                ico_name = png_file.replace('.png', '.ico')
                ico_path = os.path.join(windows_dir, ico_name)
                
                # Save as ICO
                img.save(ico_path, format='ICO')
                print(f"✓ Converted: {png_file} → {ico_name}")
                converted_count += 1
                
        except Exception as e:
            print(f"✗ Error converting {png_file}: {e}")
    
    print(f"\nConversion complete! {converted_count}/{len(png_files)} files converted successfully.")
    print(f"ICO files saved to: {windows_dir}")

if __name__ == "__main__":
    convert_png_to_ico()