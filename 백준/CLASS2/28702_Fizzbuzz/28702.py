from sys import stdin
stdin = open('input.txt')

# 15 배수 -> FizzBuzz
# 3  배수 -> Fizz
# 5  배수 -> Buzz
# 그   외 -> i

numbers = [stdin.readline().rstrip() for _ in range(3)]

for i,num in enumerate(numbers):
    if num.isdigit():
        if i == 0:
            ans = int(num) + 3
        elif i == 1:
            ans = int(num) + 2
        elif i == 2:
            ans = int(num) + 1

        if ans % 3 == 0 and ans % 5 == 0:
            print("FizzBuzz")
        elif ans % 3 == 0:
            print("Fizz")
        elif ans % 5 == 0:
            print("Buzz")
        else:
            print(ans)
        break
