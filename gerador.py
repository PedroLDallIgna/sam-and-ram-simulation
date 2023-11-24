import random
import string

def generate_random_words(n):
    words = set()
    alphabet = string.ascii_lowercase  # Letras minúsculas do alfabeto

    while len(words) < n:
        word = ''.join(random.choice(alphabet) for _ in range(random.randint(3, 8)))  # Gera uma palavra aleatória de tamanho entre 3 e 8 letras
        word+='\n'
        words.add(word)

    return list(words)

n = 500000  # Número de palavras aleatórias desejadas
random_words = generate_random_words(n)

with open("words.txt", "w") as file:
   file.writelines(random_words)
