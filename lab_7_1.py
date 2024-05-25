def count_ways_to_climb(n):
    if n <= 1:
        return 1
    ways = [0] * (n + 1)
    ways[0] = 1
    ways[1] = 1

    for i in range(2, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]

    return ways[n]


def print_ways_to_climb(n):
    if n <= 1:
        return [str(n)]
    ways = [[] for _ in range(n + 1)]
    ways[0] = ['']
    ways[1] = ['1']

    for i in range(2, n + 1):
        ways[i].extend([f'1 {way}' for way in ways[i - 1]])
        ways[i].extend([f'2 {way}' for way in ways[i - 2]])

    return ways[n]


if __name__ == '__main__':
    stairs = int(input("Введите количество ступенек: "))
    print(
        f"Количество способов подняться на {stairs} ступеньку(и): {count_ways_to_climb(stairs)}")
    print("Способы подняться:")
    for way in print_ways_to_climb(stairs):
        print(way)
