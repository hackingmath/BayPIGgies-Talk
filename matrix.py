import numpy as np

'''rotates an object to face a point'''

def matrixRotate(matA,point):
    rot_angle = np.arctan2(matA[0][1] - point[1],point[0] - matA[0][0])
    horiz = matA[0][0]
    vert = matA[0][1]
    matA = horizTranslate(matA,-horiz)
    matA = vertTranslate(matA, -vert)
    matA = rotateMatrix(matA, rot_angle)
    matA = horizTranslate(matA,horiz)
    matA = vertTranslate(matA, vert)
    return matA

def horizTranslate(matA, horizDist):
    horiz_mat = np.array([[1.0, 0.0, 0.0],
                          [0.0, 1.0, 0.0],
                          [horizDist, 0.0,1.0]])
    return np.dot(matA,horiz_mat)

def vertTranslate(matA, vertDist):
    vert_mat = np.array([[1.0, 0.0, 0.0],
                          [0.0, 1.0, 0.0],
                          [0.0, vertDist,1.0]])
    return np.dot(matA,vert_mat)

def rotateMatrix(matA,theta):
    r_matrix = np.array([[np.cos(theta), -np.sin(theta),0],
                        [np.sin(theta),np.cos(theta),0],
                        [0,    0,    1]])
    return np.dot(matA,r_matrix)
