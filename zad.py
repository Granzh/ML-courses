import random
import string
from itertools import product
from itertools import product

def generate_file():
    random_string = ''.join(random.choices(string.ascii_lowercase, k=100000))
    
    with open('random_text.txt', 'w') as f:
        f.write(random_string)

def find_longest_sequence():
    with open('random_text.txt', 'r') as f:
        text = f.read()
    
    max_length = 1
    current_length = 1
    max_char = text[0]
    
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            current_length += 1
            if current_length > max_length:
                max_length = current_length
                max_char = text[i]
        else:
            current_length = 1
    
    return max_char, max_length

# Основная программа
generate_file()
char, length = find_longest_sequence()
print(f'"{char}": {length}')

def calculate_sequence_ratio(text, k):
    
    actual_sequences = set()
    for i in range(len(text) - k + 1):
        sequence = text[i:i+k].lower()
        actual_sequences.add(sequence)
    
    ratio = len(actual_sequences)
    return ratio

with open('random_text.txt', 'r') as file:
    text = file.read()
    k = 4
    result = calculate_sequence_ratio(text, k)
    all_possible = set()
    all_possible = set(''.join(p) for p in product('abcdefghijklmnopqrstuvwxyz', repeat=k))
    print(f"Доля встречающихся последовательностей длины {k}: {result} / всего возможных: {len(all_possible)}")