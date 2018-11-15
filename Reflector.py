from random import shuffle, choice
from copy import copy
import string


class Reflector():
    maps_preset = {'A': 'EJMZALYXVBWFCRQUONTSPIKHGD',
                        'B': 'YRUHQSLDPXNGOKMIEBFZCWVJAT',
                        'C': 'FVPJIAOYEDRZXWGCTKUQSBNMHL'}
    def __init__(self, let_map):
        let_map = self.generate_map(let_map)
        self.__let_map = let_map
        self.__shift = 0

    @property
    def let_map(self):
        return self.__let_map

    @let_map.setter
    def let_map(self, x):
        self.__let_map = x

    @property
    def shift(self):
        return self.__shift

    @shift.setter
    def shift(self, x):
        self.__shift = x

    def show_char_map(self):
        for i, j in self.let_map.items():
            print(i, " -> ", j)

    @staticmethod
    def number_to_letter(x):
        ''' 65 - 91'''
        return chr(x + 64)

    @staticmethod
    def letter_to_number(x):
        return ord(x) - 64

    def generate_map(self, let_map):
        map_type = let_map if len(let_map) < 26 else 'custom'
        new_map = {}
        l = string.ascii_uppercase
        random_list = list(copy(l))
        shuffle(random_list)
        random_list = ''.join(random_list)
        maps = {'custom': let_map,
                            'random': random_list}
        maps_preset = {**maps, **self.maps_preset}
        int_list = l
        int_list2 = maps_preset[map_type]

        for i in range(len(int_list)):
            new_map[int_list[i]] = int_list2[i]
        return new_map

    def encrypt_letter(self, letter):
        answer = self.let_map[letter]
        return answer
