vec1 = [1, 2, 3, 4]
vec2 = [1, 2, 3, 4]
mat1 = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
mat2 = [[1], [2], [3]]
mat3 = [[1, 2, 3]]

def list_dot(u, v):
    return sum([u[i]*v[i] for i in range(len(u))])

def vector_addition(u, v):
    return [u[i] + v[i] for i in range(len(u))]

def matrix_checker(u, v):
    assert len(u) == len(v[0])


print(list_dot([1, 2, 3], [1, 2, 3]))
print(vector_addition(vec1, vec2))
print(matrix_checker(mat1, mat3))