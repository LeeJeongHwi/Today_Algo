from sys import stdin
stdin = open('input.txt')

inputs = stdin.readline()

def solution(inputs):
    boards = inputs.split(".")
    answer = []
    for board in boards:
        chA = board.replace("XXXX","AAAA")
        chAB = chA.replace("XX","BB")
        if "X" in chAB:
            chB = board.replace("XX","BB")
            if "X" in chB:
                return -1
            else:
                answer.append(chB)
        else:
            answer.append(chAB)
    return ".".join(answer)

print(solution(inputs))

print(solution("XX.XX"))
print(solution("XX.XXXXXX....XX"))
print(solution("XX.XXXXXXXXXX..XXXXXXXX...XXXXXX"))
