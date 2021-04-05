import time
ls = [1]*10000000

count = 0
s = time.time()
for i in ls:
    if i == 1:
        count += 1
e = time.time()
print(f"first: {e-s}")

s = time.time()
ls.count(1)
e = time.time()
print(f"second: {e-s}")
