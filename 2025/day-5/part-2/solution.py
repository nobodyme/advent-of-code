def get_all_count(ing_ranges):
    total_count = 0
    prev_range = [0, 0]

    for cur_range in ing_ranges:
        diff = 0
        if cur_range[1] > prev_range[1]:
            if cur_range[0] <= prev_range[1]:
                diff = prev_range[1] - cur_range[0] + 1
            cur_count = cur_range[1] - cur_range[0] + 1 - diff
            prev_range = cur_range
        
            total_count += cur_count
            print(f'{cur_range} = {cur_count} == {total_count}')

    return total_count

def sort_and_int_ranges(ing_ranges):
    for i in range(len(ing_ranges)):
        ing_ranges[i] = ing_ranges[i].split("-")
        ing_ranges[i] = [int(ing_ranges[i][0]), int(ing_ranges[i][1])]

    for i in range(len(ing_ranges)):
        for j in range(i + 1, len(ing_ranges)):
            if ing_ranges[j][0] < ing_ranges[i][0]:
                ing_ranges[i], ing_ranges[j] = ing_ranges[j], ing_ranges[i]

    return ing_ranges

input_file = '../input.txt'
ing_ranges = []
with open(input_file) as f:
    ing_ranges = f.read().splitlines()

# print(f"sort_ranges - {ing_ranges}\n\n")
sorted_ing_ranges = sort_and_int_ranges(ing_ranges)
print(f"sort_ranges - {sorted_ing_ranges}\n\n")

## TODO: Doesn't work
total = get_all_count(sorted_ing_ranges)
print(f"total fresh {total}")