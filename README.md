# SLAM（计算机图形学实验）
数据提供5张深度图和RGB图，及相机的内外参。  
1.读取相机内参(fx,fy,cx,cy)、外参数(R,T)，将外参的四元数转化成R矩阵；  
2.读取相机对应的深度图和RGB图，注意opencv读取RGB图的结果是BGR格式；  
3.对深度图进行处理，除以实际的尺度depth_scale=1000；  
4.遍历所有的像素，利用公式计算对应的3D点位置。  
![image](https://github.com/hjl18/SLAM/assets/79409113/ad4acbe3-31cc-4b26-80c8-e012d90c080c)
在相机有外参的情况下，可以先默认把相机放在世界坐标系原点处，转化成如下公式：  
![image](https://github.com/hjl18/SLAM/assets/79409113/d0c1dee7-0ff7-481f-9750-3ae5376b8dcb)
便可以得到每个像素(u,v)和对应的3D点坐标(x_w,y_w,z_w)，再利用相机外参数4*4的[R T]与[x_w,y_w,z_w,1]相乘即可转换到实际位置(也可旋转和平移分开进行)  
![image](https://github.com/hjl18/SLAM/assets/79409113/b5add9d3-3431-400c-b3d4-c70fb4fbdf02)
5.重复上述1-4步，将每一张图获得的点云累加；  
6.对重建的点云进行可视化(截图保存)，可以利用第三方库可视化或保存成ply等格式用meshlab软件可视化；  
7.直接拼接累加的点云往往存在噪声，需对最终的点云进行点云滤波(如统计滤波、半径滤波、体素滤波等)，这一步可使用第三方库如pcl或者open3d，对点云进行过滤，并可视化结果，需提供对比图片，可以对比不同参数的过滤结果，选择效果最好的；  
8.将最终对点云保存成ply，可以将点云信息直接写入文件，保存示例如下，也可用第三方库保存；  
![image](https://github.com/hjl18/SLAM/assets/79409113/7daeef45-ecea-42f7-a837-2fcbc55ed3b1)
如果实现正确，在滤波前你应该得到类似的结果：
![image](https://github.com/hjl18/SLAM/assets/79409113/73ce2e5b-d1a2-4b65-a8b5-8ac0783efa2f)
如果实现正确，在滤波后你应该得到类似的结果：  
![image](https://github.com/hjl18/SLAM/assets/79409113/63ba60eb-88c4-43d0-a1cc-9658d72f9c52)
