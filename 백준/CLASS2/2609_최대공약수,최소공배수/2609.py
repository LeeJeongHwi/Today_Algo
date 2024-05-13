from sys import stdin
stdin = open('input.txt')

a, b = sorted(map(int,stdin.readline().split()), reverse=True)

new_a = a
new_b = b
GCD, LCM = 0, 0
while True:
    new_a, new_b = new_b ,new_a%new_b
    if new_b == 0:
        GCD = new_a
        LCM = a*b//GCD
        break

print(GCD)
print(LCM)