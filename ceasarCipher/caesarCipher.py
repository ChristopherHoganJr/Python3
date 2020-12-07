from caesarKey import key
from caesarArt import logo
from caesarCode import caesar

print(logo)

should_continue = True

while should_continue:
    direction = input('Type \'encrypt\' to encrypt or \'decrypt\' to decrypt: ').lower()
    text = input('Type your message: ')
    shift = int(input('Type the shift number: '))
    if shift > len(key):
        shift = shift % len(key)
    caesar(start_text=text,shift_amount=shift,cipher_direction=direction)
    result = input('Type \'yes\' if you would like to go again. Type \'no\' if you are finished\n').lower()
    if result == 'no':
        should_continue = False
        print('Thank you')