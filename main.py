text = input("Введите текст: ")
text = text.lower()

punctuation = [".", ",", "!", "?"]

for symb in punctuation:
  text = text.replace(symb, '')

words = text.split()

word_frequency = {}

for word in words:
  if word in word_frequency:
    word_frequency[word] += 1
  else:
    word_frequency[word] = 1


num_words = len(set(words))

print("\nКоличество разных слов:", num_words)
print("Частота слов:")
for word, frequency in word_frequency.items():
    print(f"{word}: {frequency}")
# 1.перебрать список слов
# 2. прописать условия для проверки наличия слова в словоре
# 2. 1 +1 если слово есть, инае присвоить 1