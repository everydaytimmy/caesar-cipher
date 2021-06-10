from caesar_cipher.corpus_loader import word_list, name_list  
import re

def encrypt(plain, key):

    encrypted = ""

    for char in plain:
      if (char.isalpha()):
          if (char.isupper()):
            encrypted += chr(((ord(char) + key-65) % 26) + 65)
          else:
            encrypted += chr(((ord(char) + key-97) % 26) + 97)
      else:
        encrypted += char

    return encrypted


def decrypt(plain, key):
    return encrypt(plain, -key)

def crack(text):
  candidates = []

  for shift in range(0,26):
    possible = decrypt(text, shift)
    split_word = possible.split()
    for word in split_word:
      if (word in word_list) or (word in name_list):
        candidates.append(word)
    print(candidates)

  for phrase in candidates:
    recognized_word_count = count_words(phrase)
    potential_word_count = len(phrase.split())
    percentage = int(recognized_word_count / potential_word_count * 100)
    if percentage >= 100:
        return phrase


def count_words(text):

    candidate_words = text.split()

    word_count = 0

    for candidate in candidate_words:
        word = re.sub(r"[^A-Za-z]+", "", candidate)
        if word.lower() in word_list or word in name_list:
            word_count += 1

    return word_count