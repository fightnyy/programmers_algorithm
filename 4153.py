

if __name__ == '__main__':
    while True:
        v = list(map(int, input().split()))
        if all(s == 0 for s in v):
            break
        v.sort()
        print("right" if ((v[2] * v[2]) ==
                          (v[1]*v[1]) + (v[0] * v[0])) else "wrong")
