def list_dot(u, v):
    return sum([u[i]*v[i] for i in range(len(u))])

print(list_dot([1, 2, 3], [1, 2, 3]))