# -*- coding: utf-8 -*-
"""
@author: jankodzbanko
"""

# %%

# zacznij od instrukcji warunkowej, która sprawdzi czy długość hasła jest poprawna
# następnie przejdź do sprawdzenia warunku drugiego wykorzystując pętlę i instrukcję break

ps = 'jnhvsoics!vd'
psn = 0

for chars in ps:
    psn += 1
    if psn < 10:
        print('Hasło niepoprawne')

else: 
    for chars in ps:
        if chars != '!':
            print('Hasło niepoprawne')
        else: print('Hasło poprawne')



# %%

ps = 'jnhvsoics!vd'

if len(ps) > 10:
    for chars in ps:
        if '!' in ps:
            print('Hasło poprawne')
            break
        else: print('Hasło niepoprawne')        
else: print('Hasło niepoprawne')
        
            
    
# %%

lista = [1, 2, 99, 4, 5]

for i in lista:
    if i == 99:
        continue
    print(i)
    
# %%

raw_data = '312!32134!123!23465!234534'

fixd_data = ''

for i in raw_data:
    if i != '!':
        fixd_data = fixd_data + i
    else:
        fixd_data = fixd_data + ','
print(fixd_data)
    
    
# %%

raw_data = '312!32134!123!23465!234534'

fixd_data = ''
    
for char in raw_data:
    if char == '!':
        fixd_data += ','
        continue
    fixd_data += char
print(fixd_data)
    
    
# %%

print('Witaj w systemie rejestracji.')
print('*' * 30)


nick = input('Podaj nazwę użytkownika: ')


haslo = input('Podaj hasło. Musi zawierać jeden znak specjalny, conajmniej 8 znaków: ')
while True:
    if len(haslo) < 8 and haslo.isalnum():
        x = 0
        print('Hasło niepoprawne.')
        break
    else:
        x = 1
        print('Hasło poprawne.')
        break
if x == 1: 
    pass_check = input('Powtórz hasło: ')
    if pass_check == haslo:
        print('Rejestracja kompletna.')
else:
    print('Spróbuj jeszcze raz.')

    

     
    


    



# powtorka = input('Powtórz hasło: ')    
    
# %%

numbers = [23, 12, 53, 13, 65, 1, 45]
flag = False
idx = 0
wartosc = 13

while idx < len(numbers):
    idx += 1
    if numbers[idx] == 13:
        print('Znaleziono')
        break

# %%


def sign_up(): 
    from cryptography.fernet import Fernet
    print('Welcome to signup script')
    print('*' * 30)    
    
    nick = input('Type your nickname: \n')    
    
    password = input('Type the password, at least 8 char long and 1 special char: \n')
    
    key = Fernet.generate_key()
    fernet = Fernet(key)
    with open('key.txt', 'w') as key_file:
        key_file.write(key.decode())
        
    while True:
        if len(password) < 8 and password.isalnum():
            x = 0
            y = 0
            print('Wrong password.')
            break
        else:
            x = 1
            break
        
    if x == 1: 
        pass_check = input('Repeat password: \n')
        if pass_check == password:
            enc_password = fernet.encrypt(password.encode())
            y = 1   
    
    if y == 1:
        safety_pin = input('Type safety PIN for password recovery \n')
        if len(str(safety_pin)) == 4 and str(safety_pin).isdigit():
            
            z = 1
            enc_pin = fernet.encrypt(safety_pin.encode())
            print('PIN number set')
            
        else:
            print('Wrong PIN!')
            z = 0
                            
                        
    if z == 1:
        #current_signup = '{},{},{}'.format(nick, enc_password, enc_pin)
        with open(nick + '.txt', 'w') as user_data:
            user_data.write(str(nick) + '\n' + str(enc_password) + '\n' + str(enc_pin))
            print('Signup complete, thanks.')
            
    
    else:
        print('Try again.')
        try_again = input('Want to try again? YES/NO \n')
        if try_again == 'YES':
            sign_up()
        else: print('SO BE IT!')
        
sign_up()        


# %%
    
def password_recovery():
    
    from cryptography.fernet import Fernet
    with open('key.txt', 'r') as key_file:
        key_file = key_file.readline()
    
    nick = input('Type your nickname: \n')
    user_data = ''
    with open(nick + '.txt') as user_file:
        user_data = user_file.readlines()
        input_pin = input('Type your PIN number: \n')
        enc_pin = user_data[2]
        if input_pin == fernet.decrypt(enc_pin).decode():
            print('Data is correct.')
            

        
# %%

def nick_set():
    
    nickname = input('Type your chosen nickname, at least 4 letters long, no numbers or special chars: \n')
    if len(nickname) < 5:
        print('Wrong nickname, try again')
    else:
        if nickname.isalpha():
            nickname = nickname
            x = 1
            print('Nickname set as: ' + nickname)


# %%


def password_set():
    if x == 1:
        password = input('Type your password, at least 8 characters long and 1 special char required: \n')
        while True:
            if len(password) < 8 and password.isalnum():
                print('Wrong password.')
                break
            else:
                y = 1
                break
            
# %%

def pin_set():
        
        
        
        
        
# %%

nick_set()
        
        
        
        
        
        
        
        
        
        
        
        #for line in user_data:
            #print(user_data)
            #break
            
    
    
 
# %%
from cryptography.fernet import Fernet
key = Fernet.generate_key()
fernet = Fernet(key)

nick = 'janek'
user_data = ''
with open(nick + '.txt') as user_file:
    user_data = user_file.readlines()
    
enc_pin = (user_data[2]).encode('utf-8')
print(fernet.decrypt(enc_pin).decode())

   
    
    
    
# %%
from cryptography.fernet import Fernet
key = Fernet.generate_key()
fernet = Fernet(key)

safety_pin = input('Type safety PIN for password recovery \n')
if len(str(safety_pin)) == 4 and str(safety_pin).isdigit():
    while True:
        z = 1
        enc_pin = fernet.encrypt(safety_pin.encode())
        print('PIN number set')
        break
else:
    z = 0
    print('Wrong pin')    
    
    
# %%

import getpass

pswd = ''

pswd = getpass.getpass('Type password:\n')    
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# %%    
    
    
   
    
    
    
    
    
    
    

    