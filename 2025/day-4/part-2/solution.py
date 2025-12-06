def rolls_accessible(paper_rolls):

    ROWS = len(paper_rolls)
    COLS = len(paper_rolls[0])
    directions = [(0,-1), (0,1), (-1,0), (1,0), (-1,-1), (-1,1), (1,-1), (1,1)]

    prev_total, total = -1, 0

    while prev_total != total:
        print(f'prev - {prev_total} and total - {total}')
        prev_total = total
        for r in range(ROWS):
                for c in range(COLS):
                    occupied_count = 0

                    if paper_rolls[r][c] == "@":
                        for direction in directions:
                            
                            new_row, new_col = r + direction[0], c + direction[1]
                            if new_row < 0 or new_col < 0 or new_row >= ROWS or new_col >= COLS:
                                continue
                            
                            if paper_rolls[new_row][new_col] == "@":
                                occupied_count += 1
                            
                            if occupied_count >= 4:
                                break
                    
                        if occupied_count < 4:
                            # TODO: This can be optimized
                            s = list(paper_rolls[r])
                            s[c] = 'X'
                            paper_rolls[r] = "".join(s)
                            total += 1

        print("\n\n")
    return total

input_file = '../input.txt'
paper_rolls = []
with open(input_file) as f:
    paper_rolls = f.read().splitlines()

accessible_rolls = rolls_accessible(paper_rolls)
print("total", accessible_rolls)