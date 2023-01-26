from sys import stdin

stdin = open("input.txt","r")

n = int(stdin.readline())
eq = stdin.readline().rstrip()
st = []

operand={}

symbol = ["+","-","*","/"]
for x in eq:
    if (x not in symbol) and (x not in operand):
        operand[x] = int(stdin.readline())

result = 0

for x in eq:
    if x not in symbol:
        st.append(operand[x])
    else:
        second = st.pop()
        first = st.pop()
        re = eval(f"{first}{x}{second}")
        st.append(re)

print("{:.2f}".format(st[0]))