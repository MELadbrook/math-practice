vec1 = [1, 2, 3, 4]
vec2 = [1, 2, 3, 4]

def list_dot(u, v):
    return sum([u[i]*v[i] for i in range(len(u))])

def vector_addition(u, v):
    return [u[i] + v[i] for i in range(len(u))]

print(list_dot([1, 2, 3], [1, 2, 3]))
print(vector_addition(vec1, vec2))