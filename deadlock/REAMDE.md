### TR

#  Python ile Deadlock Simülasyonu (NYP Kavramsal Modeli)

Bu proje, kaynak gereksinimlerindeki dairesel bağımlılığın (circular dependency) neden olduğu kavramsal bir **Deadlock (Kilitlenme)** durumunu gösteren hafif bir Nesne Yönelimli Programlama (NYP) simülasyonudur.

---

##  Problem Senaryosu: Dairesel Bağımlılık

Simülasyon, birbirine bağımlı iki durumun birbirini engellediği bir kilitlenme senaryosunu modeller:
1. **Sürüş Eylemi:** Benzin istasyonuna ulaşmak için `fuel > 0` (yakıt var) şartını arar.
2. **Yakıt İkmali Eylemi:** Yakıt ekleyebilmek için önce benzin istasyonuna ulaşmış olma şartını arar.

`fuel == 0` (yakıt sıfır) olduğunda, araç yakıt almak için hareket edemez ve hareket edemediği için de yakıt alamaz — bu durum mantıksal bir **Deadlock Durumu** ile sonuçlanır.

---

### ENG

#  Deadlock Simulation in Python (OOP Conceptual Model)

A lightweight Object-Oriented Programming (OOP) simulation demonstrating a conceptual **Deadlock** state caused by circular dependency in resource requirements.

---

##  Problem Scenario: Circular Dependency
The simulation models a deadlock condition where two interdependent conditions block each other:
1. **Drive Action:** Requires `fuel > 0` to reach the gas station.
2. **Refuel Action:** Requires reaching the gas station first to add fuel.

When `fuel == 0`, the vehicle cannot drive to refuel, and cannot refuel without driving—resulting in a logical **Deadlock State**.