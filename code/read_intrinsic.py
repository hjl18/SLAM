import numpy as np
def get_intrinsic(file_path):
    intrinsic_matrices = np.zeros((3,3))
    x = 0
    with open (file_path,'r') as f:
        data = f.readlines()
        for d in data:
            d = d.strip()
            if not d or d.startswith('#'):
                continue
            d = d.split()
            intrinsic_matrices[x][0] = float(d[0])
            intrinsic_matrices[x][1] = float(d[1])
            intrinsic_matrices[x][2] = float(d[2])
            x += 1
    return intrinsic_matrices


if __name__=='__main__':
    file_path = '../data/intrinsic.txt'
    intrinsic_matrices = get_intrinsic(file_path)
    print(intrinsic_matrices)