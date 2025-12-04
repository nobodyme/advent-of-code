def find_max_volt(battery):
    rb = battery[::-1]
    
    max_a, max_al = 0, 0
    for i in range(1, len(rb)):
        if int(rb[i]) >= max_a:
            max_a = int(rb[i])
            max_al = i

    max_b = 0
    for i in range(max_al):
        max_b = max(max_b, int(rb[i]))

    print(f'{battery} = {max_a}{max_b}')

    return max_a * 10 + max_b

input_file = '../input.txt'
batteries = []
with open(input_file) as f:
    batteries = f.readlines()

total_sum = 0
for battery in batteries:
    total_sum += find_max_volt(battery.strip())

print("total", total_sum)