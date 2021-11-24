def numbers(n : int):
    if n<0:
        return
    print(n)
    numbers(n-1)
numbers(5)