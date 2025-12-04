def rotate(last_dial_num, cur_rotation):

    direction = cur_rotation[0]
    rotation_dist = int(cur_rotation[1:]) % 100

    if direction == 'R':
        cur_dial_num = last_dial_num + rotation_dist
    elif direction =='L':
        cur_dial_num = last_dial_num - rotation_dist
    
    cur_dial_num = cur_dial_num % 100
    return cur_dial_num

input_file = '../input.txt'
rotations = []
with open(input_file) as f:
    rotations = f.readlines()

total_zero = 0
last_dial_num = 50

for cur_rotation in rotations:
    last_dial_num = rotate(last_dial_num, cur_rotation)
    # print(f'cur_rotation {cur_rotation}, dial {last_dial_num}')
    if last_dial_num == 0:
        total_zero += 1

print("total_zero", total_zero)

