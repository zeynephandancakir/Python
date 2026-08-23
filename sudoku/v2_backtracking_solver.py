import os

# Dosya yolunu dinamik al
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "sudoku.txt")

matris = []
with open(file_path, "r") as file:
    for line in file:
        line = line.replace("|", "").replace("-", "").strip()
        if line:
            elements = line.split() if " " in line else list(line)
            row = [int(x) if x.isdigit() else None for x in elements]
            if row:
                matris.append(row)


def is_valid(board, row, col, num):
    """
    v1'deki kısıt kontrol mantığının aynısı:
    Seçilen sayının satır, sütun ve 3x3 bölgede olup olmadığını kontrol eder.
    """
    # Satır kontrolü
    for c in range(9):
        if board[row][c] == num:
            return False

    # Sütun kontrolü
    for r in range(9):
        if board[r][col] == num:
            return False

    # 3x3 Bölge kontrolü
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if board[r][c] == num:
                return False

    return True


def solve_sudoku_backtracking(board):
    """
    Özyinelemeli (Recursive) Backtracking Çözücü
    """
    for row in range(9):
        for col in range(9):
            if board[row][col] is None:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num

                        # ÖZYİNELEME (RECURSION): Kendini sonraki hücre için tekrar çağırır
                        if solve_sudoku_backtracking(board):
                            return True

                        # BACKTRACK: Eğer ileride tıkanırsa koyduğu sayıyı siler
                        board[row][col] = None

                # 1-9 arası hiçbir sayı uymadıysa geriye False döner (Backtrack tetiklenir)
                return False
    return True


print("--- BAŞLANGIÇ MATRİSİ ---")
for row in matris:
    print(" ".join(f"{x if x is not None else 'x':<2}" for x in row))

print("\nSudoku çözülüyor...\n")

if solve_sudoku_backtracking(matris):
    print("--- ÇÖZÜLMÜŞ MATRİS (100% BAŞARILI) ---")
    for row in matris:
        print(" ".join(f"{x:<2}" for x in row))
else:
    print("Çözüm bulunamadı!")
