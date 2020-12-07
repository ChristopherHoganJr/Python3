from caesarKey import key

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ''
    if cipher_direction == 'decrypt':
        shift_amount *= -1
    for character in start_text:
        if character in key:
            position = key.index(character)
            new_position = position + shift_amount
            if new_position > len(key):
                new_position = new_position - len(key)
            end_text += key[new_position]
        else:
            end_text += character
    print(f'The {cipher_direction}ed text is {end_text}')


    