def check_even_odd(num):
    if num % 2 == 0:
        print(f" {num} is an even number")
    else:
        print(f" {num} is an odd number")


if __name__ == "__main__":
    num = int(input("Enter your Number: "))
    check_even_odd(num)
