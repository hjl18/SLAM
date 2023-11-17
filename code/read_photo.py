import cv2
import numpy as np
def get_BGR(file_path):
    bgr_img = cv2.imread(file_path)
    return bgr_img

def get_depth(file_path):
    depth_img = cv2.imread(file_path,cv2.IMREAD_UNCHANGED)
    return depth_img

if __name__=='__main__':
    RGB_path = '../data/color/1.png'
    depth_path = '../data/depth/1.pgm'
    bgr_img = get_BGR(RGB_path)
    depth_img = get_depth(depth_path)
    #rgb_img = cv2.cvtColor(bgr_img,cv2.COLOR_BGR2RGB)
    cv2.imshow('RGB',bgr_img)
    cv2.imshow('depth',depth_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

