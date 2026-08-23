import random
alphabet={"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}
reverse_alphabet={v:k for k,v in alphabet.items()}
text=input("Enter the text you want to encrypt:").lower()
b=random.randint(0,25)

def gcd(number1,number2):
  while number2!=0:
    number1,number2=number2,number1%number2
  return number1


def generate_valid_a():
  while True:
    a=random.randint(1,25)
    if gcd(a,26)==1:
      return a
a=generate_valid_a()


def encrypt(text):
  enc_text=""
  for char in text:
    if char in alphabet:
      x = alphabet[char]
      enc_text_numerical=(a*x+b)%26
      enc_text += reverse_alphabet[enc_text_numerical]
    else:
      enc_text += char

  return enc_text

enc_text = encrypt(text) 
print("Encrypted text:", enc_text)


def mod_inverse(num1,m):
  def extended_gcd(num1,num2):
    if num1==0:
      return (num2,0,1)
    else:
      g,coeff1,coeff2=extended_gcd(num2%num1,num1)
      return (g,coeff2-(num2 // num1) * coeff1,coeff1)
  g,coeff1,coeff2=extended_gcd(num1,m)

  return coeff1 % m


def decrypt(enc_text):
  dec_text=""
  z=mod_inverse(a ,26)
  for char in enc_text:
    if char in alphabet:
      y=alphabet[char]
      dec_text_numerical=(z*(y-b)) % 26
      dec_text += reverse_alphabet[dec_text_numerical]
    else:
      dec_text +=char

  return dec_text

dec_text=decrypt(enc_text)
print("Decrypted text:",dec_text)
      
