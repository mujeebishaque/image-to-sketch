'''
Script: Image to sketch.
Author@ mujeebishaque
'''

import argparse
import cv2, os

class SketchImage():
    
    @staticmethod
    def sketch(image_path, destination):
        if not image_path or len(image_path) < 6:
            raise Exception("Check the image path provided.")
        if not destination or len(destination) < 2:
            print("\nINFO: No destination directory provided. Sketch would be saved in the current directory.")

        filename = str(image_path).split(os.sep)[-1]
        _filename, tail = filename.split('.')

        _image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        
        invert = cv2.bitwise_not(_image)  # helps in masking of the image
        blur = cv2.GaussianBlur(invert, (21, 21), 0)
        invertedblur = cv2.bitwise_not(blur)
        sketch = cv2.divide(_image, invertedblur, scale=256.0)
        
        try:
            cv2.imwrite(_filename+'_gray.'+tail, sketch)  # converted image is saved as mentioned name
        except Exception:
            raise Exception("Can't write data to the folder.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='''
    This script takes in image path and converts the image into sketch and 
    outputs to it either in the provided directory or in the current directory where this script is being executed.''', epilog="pythonvoyage.com")

    parser.add_argument('-i', '--image', required=True, type=str, help='Image path input like C:/windows/Dell/Desktop/demo.png')
    parser.add_argument('-o', '--output', required=False, type=str, help='Output path like C:/windows/Dell/Desktop/Output/image.png')

    argument = vars(parser.parse_args())

    image_path  = argument['image']
    output_path = argument['output']
    try:
        SketchImage.sketch(image_path, output_path)
    except IOError:
        raise Exception("Can't sketchify provided image.")
