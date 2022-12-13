line = '2 * 3 + 8 / 4'
line = line.split()
print(line)


def calc(sing, line1):
    for i in range(1, len(line1) - 1):
        if line1[i] == sing:
            if sing == "*":
                line1[i - 1] = int(line1[i - 1]) * int(line1[i + 1])
            elif sing == "/":
                line1[i - 1] = int(line1[i - 1]) / int(line1[i + 1])
            elif sing == "+":
                line1[i - 1] = int(line1[i - 1]) + int(line1[i + 1])
            elif sing == "-":
                line1[i - 1] = int(line1[i - 1]) - int(line1[i + 1])
            line1.pop(i + 1)
            line1.pop(i)
            break
    return line1


while len(line) > 1:
    if line.count("*"):
        line = calc("*", line)
    elif line.count("/"):
        line = calc("/", line)
    elif line.count("+"):
        line = calc("+", line)
    elif line.count("-"):
        line = calc("-", line)

print(line[0])
