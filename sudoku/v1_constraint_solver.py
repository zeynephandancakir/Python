import os
import random

# dosyanın bulunduğu klasörü alır
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "sudoku.txt")

matris = []
with open(file_path, "r") as file:
    for line in file:
        line = line.replace("|", "").replace("-", "").strip()
        if line:
            row = [int(x) if x.isdigit() else None for x in line.split()]
            matris.append(row)

for row in matris:
    print((" ".join(f"{x if x is not None else 'x':<2}" for x in row)))


def get_region(matris, row_start, col_start):
    region = []
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            region.append(matris[r][c])
    return region


region = get_region(matris, 0, 0)
print(f"region ({region}")


def solveSudoku(matris):
    for row in range(len(matris)):
        for column in range(len(matris[row])):
            cell = matris[row][column]
            if cell is None:
                constraint_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for c in range(len(matris[row])):
                    if matris[row][c] in constraint_list:
                        constraint_list = [
                            x for x in constraint_list if x != matris[row][c]
                        ]
                for r in range(len(matris)):
                    if matris[r][column] in constraint_list:
                        constraint_list = [
                            x for x in constraint_list if x != matris[r][column]
                        ]
                row_start = (row // 3) * 3
                col_start = (column // 3) * 3
                for r in range(row_start, row_start + 3):
                    for c in range(col_start, col_start + 3):
                        value = matris[r][c]
                        if value in constraint_list:
                            constraint_list = [x for x in constraint_list if x != value]

                if len(constraint_list) == 1:
                    thing = constraint_list[0]
                    matris[row][column] = thing
                    print(f"matris[{row},{column}] is:{thing}")
                elif len(constraint_list) > 1:
                    rand = random.choice(constraint_list)
                    print(f"matris[{row},{column}] is:{rand}")

                print(
                    f"for matris ({row},{column}) , constraint_list: {constraint_list}"
                )

                # DÜZELTME: Eğer kısıt listesi boş değilse rastgele seçim yap
                if len(constraint_list) > 0:
                    rand = random.randint(1, 9)
                    while rand not in constraint_list:
                        rand = random.randint(1, 9)
                    constraint_list = [x for x in constraint_list if x != rand]
                    matris[row][column] = rand
                    print(f"matris [{row},{column}] : {rand}")


solveSudoku(matris)


def check_rows(matris):
    for row, avalue in enumerate(matris):
        constraint_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for column, value in enumerate(avalue):
            if value in constraint_list:
                constraint_list = [x for x in constraint_list if x is not value]
        print(f"for row ({row}) , constraint_list: {constraint_list}")


check_rows(matris)


def check_columns(matris):
    for column in range(len(matris[0])):
        constraint_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for row in range(len(matris)):
            value = matris[row][column]
            if value in constraint_list:
                constraint_list = [y for y in constraint_list if y is not value]
        print(f"for column ({column}) , constraint_list: {constraint_list}")


check_columns(matris)
