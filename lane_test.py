import cv2
import numpy as np
import time
from fps import showfps
from showDimensions import dims
from showLines import show_lines
from show_combo_lines import combo_lines
from showFilters import filter_colors
def area_of_interest(img):
    try:
        ht = img.shape[0]
        triangle = np.array([
            [(420, 600), (1000, 600), (740, 400), (540, 400)]
        ])
        mask = np.zeros_like(img) # creating a copy of image with arrays of 0
        cv2.fillPoly(mask, triangle, 255) # function that create polygons of visible region
        masked_image = cv2.bitwise_and(img, mask) # it will hide other data and show only the visible part
        return masked_image
    except cv2.error:
        pass
    
def area_of_interest_video(img):
    triangle = np.array([
        [(280, 590), (1280, 590), (740, 320), (540, 320)]
    ])
    mask = np.zeros_like(img) # creating a copy of image with arrays of 0
    cv2.fillPoly(mask, triangle, 255) # function that create polygons of visible region
    masked_image = cv2.bitwise_and(img, mask) # it will hide other data and show only the visible part
    return masked_image

def capture(img):
    temp = 0
    lane_image = np.copy(img)
    gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY) # to convert the color from RGB to BW
    # gray = filter_colors(lane_image)
    temp = dims(gray, temp)
    blur = cv2.GaussianBlur(gray, (5, 5), 0) # to reduce the noise 
    edges = cv2.Canny(blur, 50, 150) # to find the edges
    aoi = area_of_interest(edges)
    lines = cv2.HoughLinesP(aoi, 2, np.pi/180, 100, np.array([]), 40, 5)
    avg_lines = combo_lines(lane_image, lines)
    clines = show_lines(lane_image, avg_lines)
    color_image_line = cv2.addWeighted(lane_image, 0.8, clines, 1, 1) # to merge the output with the color image
    res = cv2.resize(color_image_line, (1280, 640)) # to resize the window
    return res

def for_image():
    try:
        img = cv2.imread('test_images/test5.jpg') # to read the image file
        res = capture(img)
        cv2.imshow('Window', res) # to show the output
        cv2.waitKey(0) # to quit press q
        cv2.destroyAllWindows()
    except Exception:
        pass

def for_video():
    prev = time.time()
    fps = 0.0
    temp = 0
    cap = cv2.VideoCapture('input.mp4')
    while cap.isOpened():
        try:
            _, frame = cap.read()
            prev, fps = showfps(frame, prev, fps)
            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY) # to convert the color from RGB to BW
            # gray = filter_colors(frame)
            temp = dims(gray, temp)
            blur = cv2.GaussianBlur(gray, (5, 5), 0) # to reduce the noise 
            edges = cv2.Canny(blur, 50, 150) # to find the edges
            aoi = area_of_interest_video(edges)
            lines = cv2.HoughLinesP(aoi, 2, np.pi/180, 100, np.array([]), 40, 5)
            avg_lines= combo_lines(frame, lines)
            clines = show_lines(frame, avg_lines)
            color_image_line = cv2.addWeighted(frame, 0.9, clines, 1, 1)
            res = cv2.resize(color_image_line, (1280, 640))
            cv2.imshow('Window', res) # to show the outpqut
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break # to quit press q
        except Exception :
            pass
    cap.release()
    cv2.destroyAllWindows()
def main():
    # for_image()
    for_video()
if __name__ == "__main__":
    main()