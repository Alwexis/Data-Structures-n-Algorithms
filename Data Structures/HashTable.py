import unicodedata

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def hash_funct(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self.hash_funct(key)
        for i, (k, _) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def get(self, key):
        index = self.hash_funct(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None
    
    def remove(self, key):
        index = self.hash_funct(key)
        for i, (k, _) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False
    
    # Ejercicio 1
    def count_word_frequence(self, sentence: str):
        if len(sentence) == 0:
            return
        aux_hashtable = HashTable(20)
        # Normalizamos el String
        normalized_sentence = unicodedata.normalize('NFKD', sentence.lower())
        normalized_sentence = ''.join(c for c in normalized_sentence if not unicodedata.combining(c))
        normalized_sentence = normalized_sentence.translate(str.maketrans('', '', ",.¡!¿?"))
        for word in normalized_sentence.split(" "):
            if aux_hashtable.get(word):
                value = aux_hashtable.get(word)
                aux_hashtable.insert(word, value + 1)
            else:
                aux_hashtable.insert(word, 1)
        return aux_hashtable
    
    # Ejercicio 2
    def detect_duplicates(self, elements):
        if len(elements) == 0:
            return
        duplicates = []
        aux_hashtable = HashTable(20)
        for element in elements:
            value = aux_hashtable.get(element)
            if value:
                duplicates.append(element)
                aux_hashtable.insert(element, value + 1)
            else:
                aux_hashtable.insert(element, 1)
        return duplicates

    # Ejercicio 3
    def group_anagrams(self, anagrams):
        if len(anagrams) == 0:
            return
        aux_hashtable = HashTable(15)
        for anagram in anagrams:
            key = "".join(sorted(anagram))
            value = aux_hashtable.get(key)
            if value:
                value.append(anagram)
                aux_hashtable.insert(key, value)
            else:
                aux_hashtable.insert(key, [anagram])
        return aux_hashtable