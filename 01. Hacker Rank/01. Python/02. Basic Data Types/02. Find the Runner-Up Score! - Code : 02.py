if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l1 = list(arr)
    l1.sort(reverse=True)
    for i in range (n):
        if l1[i] > l1[i+1]:
            print(l1[i+1])
            break