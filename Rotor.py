from random import shuffle, choice
from copy import copy
from Reflector import Reflector
import string


class Rotor(Reflector):
    maps_preset = { 'I': 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
                    'II': 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
                    'III': 'BDFHJLCPRTXVZNYEIWGAKMUSQO',
                    'IV': 'ESOVPZJAYQUIRHXLNFTGKDCMWB',
                    'V': 'VZBRGITYUPSDNHLXAWMJQOFECK'}
    notch_preset = {'I': 'Q',
                         'II': 'E',
                         'III': 'V',
                         'IV': 'J',
                         'V': 'Z'}

    def __init__(self, let_map, notch=''):
        super().__init__(let_map)
        self.__notch = self.generate_notch(let_map, notch)
        self.let_map_reverse()

    @property
    def notch(self):
        return self.__notch

    @notch.setter
    def notch(self, x):
        self.__notch = x


    def move_rotor(self):
        # new_map = {}
        # for i in self.let_map.keys():
        #     new_map[self.move_key(i)] = self.move_key(self.let_map[i])
        # self.let_map = new_map
        # self.let_map_reverse()
        new_shift = self.shift + 1 if self.shift < 26 else 1

        self.shift = new_shift

    def apply_rotor(self):
        pass

    def if_notch(self):
        #print(list(self.let_map.keys())[0])
        return self.notch == self.number_to_letter(self.shift)

    @classmethod
    def move_key(cls, x, i):
        x = cls.letter_to_number(x)
        x = x + i
        if (x <= 0):
            x = 26 + x
        elif x > 26:
            x = x % 26

        y = cls.number_to_letter(x)
        return y

    def generate_notch(self, let_map, notch):
        map_type = let_map if len(let_map) < 26 else 'custom'
        l = string.ascii_uppercase
        notches = {'custom': notch,
                   'random': choice(l)}

        notches_preset = {**notches, **self.notch_preset}
        notch = notches_preset[map_type]
        return notch

    def let_map_reverse(self):
        keys = [x for x in self.let_map.values()]
        values = [x for x in self.let_map.keys()]
        self.let_map_rev = dict(zip(keys,values))

    def encrypt_letter2(self, letter):
        answer = self.let_map_rev[letter]
        return answer
