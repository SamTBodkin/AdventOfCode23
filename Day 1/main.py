input = open("Day 1\data.txt", "r")

result = 0
for x in input:
    print(x)
    line_result = ''
    for letter in range(0,len(x), 1):
        if str.isdigit(x[letter]):
            line_result = x[letter]
            print(f'first digit is {x[letter]}')
            break
    for letter in range(len(x)-1, -1, -1):
        if str.isdigit(x[letter]) :
            line_result += x[letter]
            print(f'last digit is {x[letter]}')
            break
    print(f'line result is {line_result}')
    result += int(line_result)
    print(f'total is {result}\n')

