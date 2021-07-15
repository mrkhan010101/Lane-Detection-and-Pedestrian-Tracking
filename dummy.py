# import urllib
# import cv2
# import numpy as np
# cap = cv2.VideoCapture('https://192.168.0.102:8080/shot.jpg')
# while cap.isOpened():
#     try:
#         # imgResp=urllib.urlopen(url)
#         # imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
#         # img=cv2.imdecode(imgNp,-1)
#         _, img = cap.read()
#         res = cv2.resize( img,(640, 420))
#         cv2.imshow('Window', res) # to show the outpqut
#         if cv2.waitKey(10) & 0xFF == ord('q'):
#             break # to quit press q
#     except Exception as e:
#         print(e)
# cap.release()
# cv2.destroyAllWindows()
import urllib.request
import cv2
import numpy as np

url='http://192.168.0.102:8080/shot.jpg'

while True:
    # with urllib.request.urlopen(url) as imgResp:
    imgResp = urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    res = cv2.resize( img,(640, 420))
    cv2.imshow('test', res)
    if ord('q')==cv2.waitKey(10):
        exit(0)