if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l1 = list(arr)
    l1.sort()
    print(l1[(l1.index(max(l1)))-1])