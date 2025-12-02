def rotate(last_dial_num, cur_rotation):

    direction = cur_rotation[0]
    rotation_dist = int(cur_rotation[1:]) % 100

    if direction == 'R':
        last_dial_num += rotation_dist
        if last_dial_num >= 100:
            last_dial_num -= 100
    elif direction =='L':
        last_dial_num -= rotation_dist
        if last_dial_num < 0:
            last_dial_num += 100

    return last_dial_num

input_file = 'input.txt'
rotations = []
with open(input_file) as f:
    rotations = f.readlines()

total_zero = 0
last_dial_num = 50

for cur_rotation in rotations:
    last_dial_num = rotate(last_dial_num, cur_rotation)
    if last_dial_num == 0:
        total_zero += 1

print("total_zero", total_zero)

