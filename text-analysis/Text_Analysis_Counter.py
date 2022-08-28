# https://docs.python.org/3/library/collections.html#collections.Counter
from collections import Counter

with open("text.txt", encoding="utf-8") as f:
    text = f.read()

for c in ',."':
    text = text.replace(c, '')


counts = Counter(text.split())

# Dicionário com as frequências das palavras no texto
for k, v in counts.items():
    print(f'{k} - {v}')

# As 3 palavras mais frequentes
print(counts.most_common(3))

# Número total de ocorrências
print(f'Número total de ocorrências - {sum(counts.values())} ')

# Número de ocorrências uma dada palavra
print(f'A palavra "dolor" existe {counts["dolor"]} vezes no texto.')

# Elementos ordenados
elements_sorted = set(sorted(counts.elements()))
for el in elements_sorted:
    print(el)
