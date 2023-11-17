import numpy as np

def get_extrinsic(file_path):
    with open(file_path,'r') as f:
        data = f.readlines()
        extrinsic_matrices = []
        for d in data:
            d = d.strip()
            if not d or d.startswith('#'):
                continue
            values = [float(val) for val in d.split()]
            tx, ty, tz, qx, qy, qz, qw = values[:7]
            rotation_matrix = np.array([
                [1 - 2 * qy ** 2 - 2 * qz ** 2, 2 * qx * qy - 2 * qz * qw, 2 * qx * qz + 2 * qy * qw],
                [2 * qx * qy + 2 * qz * qw, 1 - 2 * qx ** 2 - 2 * qz ** 2, 2 * qy * qz - 2 * qx * qw],
                [2 * qx * qz - 2 * qy * qw, 2 * qy * qz + 2 * qx * qw, 1 - 2 * qx ** 2 - 2 * qy ** 2]
            ])

            extrinsic_matrix = np.eye(4)
            extrinsic_matrix[:3, :3] = rotation_matrix
            extrinsic_matrix[:3, 3] = np.array([tx, ty, tz])
            extrinsic_matrices.append(extrinsic_matrix)

        extrinsic_matrices = np.array(extrinsic_matrices)
        return  extrinsic_matrices

if __name__=='__main__':
    file_path = '../data/pose.txt'
    extrinsic_matrices = get_extrinsic(file_path)
    print(extrinsic_matrices[0])