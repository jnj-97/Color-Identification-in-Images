# Color-Identification-in-Images
Using Image module functions, this code generates a text file with all  the hexadecimal color values
This has two modes, image and video
Image function uses get colors with a high max color limit from PIL function. This function releases a list of tuples containing color position and rgb value tuple. This rgb tuple is converted to hex code and writtten to a hex file
Video function converts a video into its frames and saved as .jpg images into a desired directory using computer vision cv2 functions. The images are iterated through where the image function operates on each image

