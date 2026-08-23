### TR

#  Dinamik Affine Şifreleme Uygulaması

Python ile geliştirilmiş bu proje; dinamik anahtar üretimi, matematiksel aralarında asallık doğrulaması ve **Genişletilmiş Öklid Algoritması (Extended Euclidean Algorithm)** aracılığıyla modüler ters hesaplama özelliklerine sahip bir **Affine Şifreleme** uygulamasıdır.

---

##  Özellikler ve Algoritmik Tasarım

* **Dinamik Anahtar Üretimi (`generate_valid_a`):** a anahtarının modüler çarpımsal tersinin bulunabilmesini garanti etmek için, \gcd(a, 26) = 1 şartını sağlayan geçerli bir a \in [1, 25] anahtarını otomatik olarak seçer.
* **Rastgele Kaydırma Anahtarı (`b`):** Her çalıştırma için rastgele bir kaydırma anahtarı b \in [0, 25] üretir.
* **Genişletilmiş Öklid Algoritması (`mod_inverse`):** Mesajın şifresini doğru bir şekilde çözebilmek için a^{-1} \pmod{26}$değerini dinamik olarak hesaplar.
* **Alfabe Dışı Karakter Desteği:** Dönüştürme sırasında boşlukları, noktaları ve sayıları değiştirmeden olduğu gibi korur.

---

##  Matematiksel İşlemler

1. **Şifreleme Formülü:** 
   E(x) = (a \cdot x + b) \pmod{26}
2. **Şifre Çözme Formülü:** 
   D(y) = a^{-1} \cdot (y - b) \pmod{26}

---

### ENG 

#  Dynamic Affine Cipher Implementation

A Python implementation of the **Affine Cipher** featuring dynamic key generation, mathematical coprimality validation, and modular inverse calculation via the **Extended Euclidean Algorithm**.

---

##  Features & Algorithmic Design

* **Dynamic Key Generation (`generate_valid_a`):** Automatically selects a valid key a \in [1, 25] such that \gcd(a, 26) = 1, guaranteeing that a has a modular multiplicative inverse.
* **Random Shift Key (`b`):** Generates a random shift key b \in [0, 25] for each execution.
* **Extended Euclidean Algorithm (`mod_inverse`):** Dynamically calculates a^{-1} \pmod{26} to accurately decrypt the message.
* **Non-Alphabetic Character Support:** Retains spaces, punctuation, and numbers unchanged during transformation.

---

##  Mathematical Operations

1. **Encryption Formula:** 
   E(x) = (a \cdot x + b) \pmod{26}
2. **Decryption Formula:** 
   D(y) = a^{-1} \cdot (y - b) \pmod{26}

---

##  How to Run

Run the script directly via terminal:

```bash
python AffineEncryption.py

