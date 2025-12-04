def is_invalid_num(num):
    str_num = str(num)
    len_num = len(str_num)
    
    if len_num % 2 != 0:
        return False
    
    s1, s2 = 0, int(len_num / 2)
    while s2 < len_num:
        if str_num[s1] != str_num[s2]:
            return False
        s1 += 1
        s2 += 1

    return True

def sum_invalid_range(start, end):
    sum_invalid_nums = 0
    for num in range(start, end + 1):
        if is_invalid_num(num):
            sum_invalid_nums += num

    return sum_invalid_nums

input_file = "../input.txt"
p_ranges = []
with open(input_file, "r") as f:
    p_ranges = f.read().strip().split(",")

total_sum = 0
for p_range in p_ranges:
    start, end = p_range.split("-")
    print(f"\n{start} - {end}")
    if start[0] == "0":
        print(f"sum = {0}")
        continue
    sum_i = sum_invalid_range(int(start), int(end))
    print(f"sum = {sum_i}")
    total_sum += sum_i
    
print(f"\n\ntotal_sum - {total_sum}\n")