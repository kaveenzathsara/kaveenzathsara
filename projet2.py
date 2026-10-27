#password genarator
import random


Letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')']

print("Welcome to the password generator!")
nr_letters=int(input("How many letters would you like in your password? : "))
print()
nr_numbers=int(input("How many numbers would you like in your password? : "))
print()
nr_symbols=int(input("How many symbols would you like in your password? : "))
print()

pass_size=nr_letters+nr_numbers+nr_symbols
password=[]

#for letters
for i in range(nr_letters):
    password.append(random.choice(Letters))

#for numbers
for i in range(nr_numbers):
    password.append(random.choice(numbers))

#for symbols
for i in range(nr_symbols):
    password.append(random.choice(symbols))  


random.shuffle(password)    
real_pass=""

for i in range(pass_size):
    real_pass=real_pass+password[i]
#me udata one nm real_pass = "".join(password)  ohomth puluwn thani peliyen


print("Your password is : ",real_pass)    
