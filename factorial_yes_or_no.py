while True:
    num = input("plz enter yr number : = (exit : press space)")
    if num == " ":
        break
    nn = n = int(num)

    f = i = 0
    while True:
        i += 1
        if n % i == 0:
            n = n // i
            f += 1
        if n < i:
            break
    if n == 1 and f == i or nn == 1:
        print("yes")
    else:
        print("no")

