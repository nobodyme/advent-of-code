def find_max_volt(battery, total = 12):
    rb = battery[::-1]
    max_arr = []
    max_loc = 0

    for num in range(total - 1, -1, -1):
        local_max = 0
        end = len(rb)
        if max_loc:
            end = min(end, max_loc)

        for i in range(num, end):
            if int(rb[i]) >= local_max:
                max_loc = i
                local_max = int(rb[i])
        
        max_arr.append(str(local_max))
    
    return int("".join(max_arr))

input_file = '../input.txt'
batteries = []
with open(input_file) as f:
    batteries = f.readlines()

total_sum = 0
for battery in batteries:
    l_sum = find_max_volt(battery.strip(), 12)
    print(f'{battery.strip()} - {l_sum}')
    total_sum += l_sum

print("total_sum", total_sum)