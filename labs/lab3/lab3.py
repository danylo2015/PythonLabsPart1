def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


def count_triangles(value):
    triangles = 0
    triangle_combinations = []

    for i in range(len(value)):
        for j in range(i + 1, len(value)):
            for k in range(j + 1, len(value)):
                a, b, c = value[i], value[j], value[k]
                if is_triangle(a, b, c):
                    triangles += 1
                    triangle_combinations.append((a, b, c))

    print("\nAll possible combinations:")
    for numbers_combinations in triangle_combinations:
        print(" ".join(map(str, numbers_combinations)))

    return triangles


numbers = [18, 14, 5, 6, 8, 2]
result = count_triangles(numbers)
print(f"Number of possible triangles: {result}")
