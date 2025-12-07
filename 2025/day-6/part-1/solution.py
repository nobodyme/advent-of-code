def solve(numbers):

    ROWS = len(numbers)
    COLS = len(numbers[0])

    total_sum = 0

    for col in range(COLS):
        operator = numbers[ROWS - 1][col]
        local_sum = 0
        for row in range(ROWS - 1):
            if not local_sum:
                local_sum = numbers[row][col]
            else:
                local_sum = do_the_math(local_sum, numbers[row][col], operator)
        
        total_sum += local_sum
    
    return total_sum

def do_the_math(a, b, op):
    if op == "+":
        return int(a) + int(b)
    else:
        return int(a) * int(b)

input_file = '../input.txt'
inputs = []
with open(input_file) as f:
    inputs = f.read().strip().split("\n")

numbers = []
for line in inputs:
    num = line.split()
    numbers.append(num)

result = solve(numbers)
print(result)