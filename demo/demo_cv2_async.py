#!/usr/bin/env python
import freenect
import frame_convert2
import ConvNet as CNN
import cv2
import pdb
import time
#import matplotlib.pyplot as plt
"""

cv2.namedWindow('Depth')
cv2.namedWindow('RGB')
"""
keep_running = True

def display_depth(dev, data, timestamp):
    pass
#    global keep_running
#    cv2.imshow('Depth', frame_convert2.pretty_depth_cv(data))
#    if cv2.waitKey(10) == 27:
#        keep_running = False
    

def display_rgb(dev, data, timestamp):
#    pass
    global keep_running
    im = frame_convert2.video_cv(data)
#    im = im_or.copy()
#    pdb.set_trace()
    if len(im) is not 0:
        cls,det = CNN.detect(net,im)
#    print(det[0,0:4])
        print det.shape
#    time.sleep(0.1)
#    pdb.set_trace()
#        CNN.vis_detections(im,cls,det)
#    print det
#    plt.imshow(im)
#    plt.show()
#    pdb.set_trace()
#    cv2.imshow('RGB', im)
#    if cv2.waitKey(10) == 27:
#        keep_running = False


def body(*args):
    if not keep_running:
        raise freenect.Kill


net = CNN.setupNet()

print('Press ESC in window to stop')
freenect.runloop(depth=display_depth,
                 video=display_rgb,
                  body=body)
