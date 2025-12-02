def rotate(last_dial_num, cur_rotation):

    zero_count = 0
    direction = cur_rotation[0]
    rotation_dist = int(cur_rotation[1:])
    zero_count = int(rotation_dist / 100)
    rotation_dist = rotation_dist % 100

    if direction == 'R':
        cur_dial_num = last_dial_num + rotation_dist
    elif direction =='L':
        cur_dial_num = last_dial_num - rotation_dist
    
    if (last_dial_num > 0 and cur_dial_num < 0) or cur_dial_num > 100:
        zero_count += 1

    cur_dial_num = cur_dial_num % 100
    if cur_dial_num == 0:
        zero_count += 1

    print(f"\n{cur_rotation.strip()} to {cur_dial_num} zero_c {zero_count}")
    return zero_count, cur_dial_num

input_file = 'input.txt'
rotations = []
with open(input_file) as f:
    rotations = f.readlines()

total_zero_crossed = 0
last_dial_num = 50

for cur_rotation in rotations:
    zero_count, last_dial_num = rotate(last_dial_num, cur_rotation)
    total_zero_crossed += zero_count

print("total_zero_crossed", total_zero_crossed)

