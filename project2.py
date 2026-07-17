import random
letters=['q','w','e','r','t','y','u','i','o','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','$','%','^','&','*','(',')','+']
print("Welcome to Password Generator!")
n_letters=int(input("How many letters you want in your password?\n"))
n_numbers=int(input("How many numbers you want in your password?\n"))
n_symbols=int(input("How many symbols you want in your password?\n"))
password_l=[]
for i in range(1,n_letters+1):
    char=random.choice(letters)
    password_l+=char
for i in range(1,n_numbers+1):
    char=random.choice(numbers)
    password_l+=char
for i in range(1,n_symbols+1):
    char=random.choice(symbols)
    password_l+=char
password=""
for i in password_l:
    password+=i
print("Password:",password)




