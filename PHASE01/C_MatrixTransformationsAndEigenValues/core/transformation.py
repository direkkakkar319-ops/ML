"""Transformation matrices from scratch (Python)"""
import math 

"""Rotation of matrix"""
def rotation_2d(theta):
    c,s = math.cos(theta), math.sin(theta)
    return [[c,-s], [s,c]]

"""Scaling"""
def scaling_2d(sx, sy):
    return [[sx,0],[0, sy]]

"""Shearing"""
def shearing_2d(kx, ky):
    return [[1,kx], [ky,1]]

"""Reflection""" 
def reflection_x():
    return [[1,0],[0,-1]]
def reflection_y():
    return [[-1,0], [0,1]]

"""Matrix multiplication with vectors"""
def mat_vec_mul(matrix, vector):
    return [
        sum(matrix[i][j] * vector[j] for j in range(len(vector)))
        for i in range(len(matrix)) 
    ]

"""Matrix multiplication""" 
def mat_mul(a, b):
    rows_a, cols_a = len(a), len(a[0])
    rows_b, cols_b = len(b), len(b[0])

    if cols_a != rows_b:
        raise ValueError("Incompatible dimensions")

    return [
        [
            sum(a[i][k] * b[k][j] for k in range(cols_a))
            for j in range(cols_b)
        ]
        for i in range(rows_a)
    ]

"""Using the functions"""
point=[1.0,0.0]
angle=math.pi/4

rotated=mat_vec_mul(rotation_2d(angle), point)
print(f"Rotate{point} by 45 deg:({rotated[0]:.4f}, {rotated[1]:.4f})") 

scaled = mat_vec_mul(scaling_2d(2, 3), [1.0, 1.0])
print(f"Scale (1,1) by (2,3): ({scaled[0]:.1f}, {scaled[1]:.1f})")

sheared = mat_vec_mul(shearing_2d(1, 0), [1.0, 1.0])
print(f"Shear (1,1) kx=1: ({sheared[0]:.1f}, {sheared[1]:.1f})")

reflected_y = mat_vec_mul(reflection_y(), [2.0, 1.0])
print(f"Reflect (2,1) across y: ({reflected_y[0]:.1f}, {reflected_y[1]:.1f})")

reflected_x = mat_vec_mul(reflection_x(), [2.0, 1.0])
print(f"Reflect (2,1) across x: ({reflected_x[0]:.1f}, {reflected_x[1]:.1f})") 

"""Composition of transformations"""
R = rotation_2d(math.pi / 2)
S = scaling_2d(2, 0.5)

rotate_then_scale = mat_mul(S, R)
scale_then_rotate = mat_mul(R, S)

point = [1.0, 0.0]
result1 = mat_vec_mul(rotate_then_scale, point)
result2 = mat_vec_mul(scale_then_rotate, point)

print(f"Rotate 90 then scale: ({result1[0]:.2f}, {result1[1]:.2f})")
print(f"Scale then rotate 90: ({result2[0]:.2f}, {result2[1]:.2f})")
print(f"Same? {result1 == result2}") #shows that matrix multiplication is not commutative