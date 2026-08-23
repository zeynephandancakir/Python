### TR

#  Algoritmik Sudoku Çözücü: Kısıt Sağlama ve Backtracking Evrimi

Bu proje, Python ile geliştirilmiş otomatik bir Sudoku çözücünün analitik tasarımını ve adım adım gelişimini göstermektedir. Standart bir **Kısıt Sağlama Stratejisinden (Constraint Satisfaction Strategy)** güçlü bir **Özyinelemeli Geri Adım Atma (Recursive Backtracking)** algoritmasına geçiş sürecini belgeler.

##  Proje Genel Bakış

Sudoku, her bir hücrenin aşağıdaki kurallara göre 1 ile 9 arasında bir rakamla doldurulması gereken kısıt-sağlama tabanlı bir bulmacadır:
1. Her satır 1'den 9'a kadar benzersiz rakamlar içermelidir.
2. Her sütun 1'den 9'a kadar benzersiz rakamlar içermelidir.
3. Her 3x3'lük alt bölge (region) 1'den 9'a kadar benzersiz rakamlar içermelidir.

Bu depo; problem analizini, kenar durum (edge-case) ayıklamasını ve algoritma optimizasyonunu ön plana çıkararak basit kısıt-indirgeme yaklaşımı ile özyinelemeli backtracking çözücüyü karşılaştırır.

---

##  Klasör Yapısı

* `sudoku.txt` — Çözülecek ham girdi matris verisi.
* `v1_naive_constraint_solver.py` — Satır, sütun ve 3x3 bölge kısıtlamalarını hesaplayan ilk sezgisel yaklaşım.
* `v2_backtracking_solver.py` — Kısıt doğrulama yapısına özyineleme ve backtracking entegre eden tam çözücü.

---

##  Mimari ve Evrimsel Yaklaşımlar

**v1: Basit Kısıt Çözücü (Yarım Kalan Matris)**
* Aday listelerini (1-9) değerlendirir.
* Seçimleri rastgele yapar.
* Aday liste boşaldığında kilitlenir (Deadlock).

**v2: Backtracking Çözücü (%100 Çözülmüş Matris)**
* Kısıtları dinamik olarak değerlendirir.
* Özyineleme (Recursion) kullanır.
* Kilitlenme durumlarında geriye adımlar (Backtrack).

### 1. Sürüm 1: Basit Kısıt Çözücü (`v1_naive_constraint_solver.py`)
* **Strateji:** Satır, sütun ve 3x3'lük alt bölgede zaten var olan rakamları eleyerek boş her hücre için geçerli adayları değerlendirir.
* **Sınırlama:** Bir kilitlenme yaşandığında (`constraint_list = []`) önceki seçimleri geri alma mekanizmasından yoksundur. Erken aşamada yanlış bir seçim yapılırsa program bunu düzeltemez.

### 2. Sürüm 2: Özyinelemeli Backtracking Çözücü (`v2_backtracking_solver.py`)
* **Strateji:** `v1`'deki kısıt doğrulama mantığını (`is_valid`) birebir korur ancak bunu özyinelemeli bir durum-uzayı arama (state-space search) algoritmasıyla sarmalar.
* **Sonuç:** Bir hücre kilitlenmeyle karşılaştığında fonksiyon `False` döner; bu da çağrı yığınının (call stack) önceki karar durumuna **geri adım atmasına (backtrack)**, geçersiz girdiyi temizlemesine ve eksiksiz geçerli bir çözüm bulunana kadar bir sonraki aday rakamı denemesine olanak tanır.

---

##  Nasıl Çalıştırılır

1. Depoyu klonlayın:
   ```bash
   git clone [https://github.com/kullanici-adiniz/sudoku-solver.git](https://github.com/kullanici-adiniz/sudoku-solver.git)
   cd sudoku-solver

### ENG 

# Algorithmic Sudoku Solver: Constraint Satisfaction & Backtracking Evolution

This project demonstrates the analytical design and evolutionary development of an automated Sudoku solver in Python. It documents the transition from a standard **Constraint Satisfaction Strategy** to a robust **Recursive Backtracking Algorithm**.

##  Project Overview

Sudoku is a constraint-satisfaction puzzle where each cell must be filled with a digit from 1 to 9 such that:
1. Each row contains unique digits from 1 to 9.
2. Each column contains unique digits from 1 to 9.
3. Each 3 * 3 sub-grid (region) contains unique digits from 1 to 9.

This repository contrasts a naive constraint-reduction approach against a recursive backtracking solver, highlighting problem analysis, edge-case debugging, and algorithm optimization.

---

##  Folder Structure

* `sudoku.txt` — Raw input matrix data to be solved.
* `v1_naive_constraint_solver.py` — Initial heuristic approach calculating row, column, and 3x3 region constraints.
* `v2_backtracking_solver.py` — Complete solver integrating recursion and backtracking into constraint validation.

---

##  Architecture & Evolutionary Approaches

v1 : Naive Constraint Solver (Incomplete Grid): 
* Evaluates candidate lists(1-9).
* Chooses randomly.
* Deadlocks when empty.

v2 : Backtracking Solver (100% Solved Grid):

* Evaluates constraints dynamically.
* Uses Recursion.
* Reverts on deadlocks.

### 1. Version 1: Naive Constraint Solver (`v1_naive_constraint_solver.py`)
* **Strategy:** Evaluates valid candidates for each empty cell by filtering out digits already present in its row, column, and $3 \times 3$ sub-grid.
* **Limitation:** Lacks a mechanism to revert previous choices when a deadlock occurs (`constraint_list = []`). If an incorrect choice is made early on, the program cannot recover.

### 2. Version 2: Recursive Backtracking Solver (`v2_backtracking_solver.py`)
* **Strategy:** Retains the exact constraint validation logic from `v1` (`is_valid`) but wraps it in a recursive state-space search algorithm.
* **Outcome:** When a cell encounters a deadlock, the function returns `False`, causing the call stack to **backtrack** to the previous decision state, clear the invalid entry, and attempt the next candidate digit until a complete valid solution is found.

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/sudoku-solver.git](https://github.com/your-username/sudoku-solver.git)
   cd sudoku-solver