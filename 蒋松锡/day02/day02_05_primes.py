count = 0

for n in range(101, 201):
    is_prime = True

    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n)
        count += 1

print ("总数：", count)