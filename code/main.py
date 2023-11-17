import numpy as np
import os
import open3d as o3d
import read_intrinsic as ri
import read_extrinsic as re
import read_photo as rp
import create_cloud as cc

def main(rgb_list,depth_list,intrinsic_path,pose_path):
    depth_scale = 1000
    intrsinc_matrix = ri.get_intrinsic(intrinsic_path)
    fx = intrsinc_matrix[0][0]
    fy = intrsinc_matrix[1][1]
    cx = intrsinc_matrix[0][2]
    cy = intrsinc_matrix[1][2]
    extrinsic_matrices = re.get_extrinsic(pose_path)
    points = list()
    rgb_length = len(rgb_list)
    depth_length = len(depth_list)
    assert rgb_length==depth_length,"RGB图像与深度图数量不相等"

    for i in range(depth_length):
        bgr_img = rp.get_BGR(rgb_list[i])
        depth_img = rp.get_depth(depth_list[i])
        extrinsic_matrix = extrinsic_matrices[i]
        for u in range(depth_img.shape[0]):
            for v in range(depth_img.shape[1]):
                depth = depth_img[u][v]
                if depth <= 0:
                    continue
                axis = cc.cal_axis(u,v,depth,fx,fy,cx,cy,extrinsic_matrix,depth_scale)
                cloud_bgr = cc.cal_rgb(bgr_img,u,v)
                point = [axis[0],axis[1],axis[2],cloud_bgr[2],cloud_bgr[1],cloud_bgr[0]]
                points.append(point)
    points = np.array(points)

    xyz = points[:, :3]
    rgb = points[:, 3:]

    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(xyz)
    pcd.colors = o3d.utility.Vector3dVector(rgb / 255.0)  # 归一化RGB值到范围[0, 1]
    print("滤波前点云数量：",len(pcd.points))
    # o3d.visualization.draw_geometries([pcd])

    # 统计滤波
    pcd_sta_filtered = pcd.remove_statistical_outlier(nb_neighbors=2,std_ratio=0.5)
    print("统计滤波后点云数量：",len(pcd_sta_filtered[0].points))
    # o3d.visualization.draw_geometries([pcd,pcd_sta_filtered])

    # 半径滤波
    pcd_ra_filtered = pcd.remove_radius_outlier(nb_points=5, radius=0.5)
    print("半径滤波后点云数量：", len(pcd_sta_filtered[0].points))
    o3d.visualization.draw_geometries([pcd, pcd_ra_filtered])

    # 体素下滤波
    downsampled_pcd = pcd.voxel_down_sample(voxel_size=2.0)
    print("体素下滤波后点云数量：", len(downsampled_pcd[0].points))
    o3d.visualization.draw_geometries([pcd, downsampled_pcd])

if __name__=='__main__':
    intrinsic_path = '../data/intrinsic.txt'
    pose_path = '../data/pose.txt'
    color_path = '../data/color/'
    depth_path = '../data/depth/'
    rgb_list = [color_path+file for file in os.listdir(color_path) if os.path.isfile(os.path.join(color_path, file))]
    depth_list = [depth_path+file for file in os.listdir(depth_path) if os.path.isfile(os.path.join(depth_path, file))]
    print('rgb_list:',rgb_list)
    print('depth_list:',depth_list)
    main(rgb_list,depth_list,intrinsic_path,pose_path)


