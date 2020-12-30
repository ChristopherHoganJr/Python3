import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

# Dictionary Comprehension
nato = {row.letter:row.code for (index, row) in data.iterrows()}
# Ask user to input a word
word = input("Enter a word: ").upper()
# Create a list of values for the letters in users word
nato_phonetic = [nato[i] for i in word]

print(nato_phonetic)