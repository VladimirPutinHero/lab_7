def count_routes(n, m):

    routes = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        routes[i][0] = 1

    for j in range(m):
        routes[0][j] = 1

    for i in range(1, n):
        for j in range(1, m):

            routes[i][j] = routes[i - 1][j] + routes[i][j - 1]

    return routes[n - 1][m - 1]


if __name__ == "__main__":
    n = int(input("Введите количество ячеек по вертикали: "))
    m = int(input("Введите количество ячеек по горизонтали: "))

    print(
        f"Количество маршрутов из левого верхнего угла в правый нижний: {count_routes(n, m)}")
