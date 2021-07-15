import urllib.request
import cv2
import numpy as np
import math
import time
from fps import showfps
from showLines import show_lines
from show_combo_lines import combo_lines

def area_of_interest_video(img):
    ht = img.shape[0]
    # Co-ordinates of viewing triangele
    triangle = np.array([   
        [(0, ht), (2560, ht), (546, 50)]
    ])
    mask = np.zeros_like(img) # creating a copy of image with arrays of 0
    cv2.fillPoly(mask, triangle, 255) # function that create polygons of visible region
    masked_image = cv2.bitwise_and(img, mask) # it will hide other data and show only the visible part
    return masked_image

def for_video():
    prev = time.time()
    fps = 0.0
    url='http://192.168.0.102:8080/shot.jpg'
    # cap = cv2.VideoCapture('rtsp//:192.168.0.102:8080')
    while True:
        try:
            imgResp = urllib.request.urlopen(url)
            imgNp =np.array(bytearray(imgResp.read()),dtype=np.uint8)
            frame =cv2.imdecode(imgNp,-1)
            prev, fps = showfps(frame, prev, fps)
            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY) # to convert the color from RGB to BW
            blur = cv2.GaussianBlur(gray, (5, 5), 0) # to reduce the noise 
            edges = cv2.Canny(blur, 50, 150) # to find the edges
            aoi = area_of_interest_video(edges)
            lines = cv2.HoughLinesP(aoi, 2, np.pi/180, 100, np.array([]), 40, 5)
            avg_lines = combo_lines(frame, lines)
            clines = show_lines(frame, avg_lines)
            color_image_line = cv2.addWeighted(frame, 0.9, clines, 1, 1)
            res = cv2.resize(color_image_line, (480, 240))
            cv2.imshow('Window', res) # to show the outpqut
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break # to quit press q
        except Exception:
            pass

def main():
    for_video()
    
if __name__ == "__main__":
    main()
