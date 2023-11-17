import numpy as np


#u-->y(row),v-->x(col)
def cal_axis(u,v,d,fx,fy,cx,cy,extrinsic,depth_scale):
    z = d / depth_scale
    x = (v - cx) * z / fx
    y = (u - cy) * z / fy
    axis_init = np.array([x,y,z,1]).reshape(-1, 1)
    axis = np.dot(extrinsic,axis_init)
    return axis

def cal_rgb(bgr_img,u,v):
    b = bgr_img[u][v][0]
    g = bgr_img[u][v][1]
    r = bgr_img[u][v][2]
    cloud_bgr = np.array([b,g,r])
    return cloud_bgr