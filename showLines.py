import cv2
import numpy as np
def show_lines(img, lines):
    line_image = np.zeros_like(img) # creating a copy of image with arrays of 0
    if lines is not None:
        for line in lines:
            try:
                x1, y1, x2, y2 = line.reshape(4) # spliting 4 array element
                if(x1 > 2000 or x2 > 2000):
                    x1 = 1920
                    x2 = 1920
                    cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 10)
                else:
                    cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 10)
            except Exception:
                pass
    return line_image
    