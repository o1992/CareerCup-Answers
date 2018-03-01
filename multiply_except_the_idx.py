def multiply_except_index(arr):
    front = len(arr) * [0]
    front[0] = 1
    rear = len(arr) * [0]
    rear[-1] = 1
    sol = list()
    for i in range(1, len(front)):
        front[i] = front[i - 1] * arr[i - 1]
    for i in range(len(rear) - 2, -1, -1):
        rear[i] = rear[i + 1] * arr[i + 1]
    for i in range(0, len(arr)):
        sol.append(rear[i] * front[i])
    print(sol)


arr = [2, 3, 1, 4]
multiply_except_index(arr)