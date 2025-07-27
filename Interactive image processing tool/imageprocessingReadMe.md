# INTERACTIVE IMAGE PROCESSING TOOL

A command-line tool built with OpenCV and NumPy that lets users apply various transformations to an image—like grayscale conversion, binary thresholding (black & white), cropping, flipping, rotation, resizing, blurring, and sharpening.

# FEATURES

1. Convert to Grayscale — shows soft gradients in gray tones

2.  Convert to Black & White — pure black and white with no shading

3. Crop using custom coordinates

4.  Flip vertically, horizontally, or both

5. Rotate by any angle

6. Blur the image using Gaussian filtering

7. Sharpen with kernel enhancement

8. Resize to new dimensions

9. Save with auto-generated timestamped filenames

10. Friendly CLI prompts for a smooth workflow

# REQUIREMENTS

1. Python 3.x

2. OpenCV

3. NumPy

4. os(built in)

5. time(built in)

Install dependencies using pip:
pip install opencv-python numpy



# HOW TO USE

1. Run the script in a Python environment.

2. Enter the full path of the image you want to process.

3. Choose from the menu:

4. Type 1 for Gray Scale - shows soft gradients in gray tones

5. Type 2 for Black & White - pure contrast, no shading

6. Type 3 to Crop the image

7. Type 4 to Flip the image

8. Type 5 to Rotate the image

9. Type 6 to Blur the image

10. Type 7 to Sharpen the image

11. Type 8 to Resize the image

12. Preview the final result in a pop-up window.

13. After processing, decide if you want to save the image:

14. If yes, the output will be saved in the current directory with a name like:
photo-25-07-27 16 14 15.jpg

# TERMINOLOGY TIP

Grayscale = 256 shades of gray (preserves detail and texture)

Black & White = Binary output, only black or white pixels (no gradients)

Many users confuse these two—this tool helps clarify and visualize the difference!
Cropping guides you based on image dimensions

Time-stamped filenames avoid overwrite and support versioning

