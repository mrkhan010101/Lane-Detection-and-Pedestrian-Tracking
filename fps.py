import cv2
import time
FPS_SMOOTHING = 0.9

def showfps(frame, prev, fps): 
    now = time.time()
    fps = (fps*FPS_SMOOTHING + (1/(now - prev))*(1.0 - FPS_SMOOTHING))
    # print("fps: {:.1f}".format(fps))
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(frame, "fps: {:.1f}".format(fps), (246, 26), font, 0.5, (0, 255, 0), 1)
    return now, fps