def get_fresh_count(ing_ranges, ingredients):
    range_index = 0
    fresh_count = 0

    for cur_ingredient in ingredients:
        print(f'finding {cur_ingredient}')
        while range_index < len(ing_ranges):
            if cur_ingredient < ing_ranges[range_index][0]:
                break

            if cur_ingredient > ing_ranges[range_index][1]:
                range_index += 1
                continue
            
            if cur_ingredient >= ing_ranges[range_index][0] and cur_ingredient <= ing_ranges[range_index][1]:
                fresh_count += 1
                break

    return fresh_count

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
with open(input_file) as f:
    block1, block2 = f.read().strip().split("\n\n", 1)

ing_ranges = block1.splitlines()
sorted_ing_ranges = sort_and_int_ranges(ing_ranges)

ingredients = block2.splitlines()
ingredients = [int(num) for num in ingredients]
ingredients.sort()

print(f"sort_ranges - {sorted_ing_ranges}\n\n")
print(f"ingredients - {ingredients}\n\n")

total = get_fresh_count(sorted_ing_ranges, ingredients)
print(f"total fresh {total}")