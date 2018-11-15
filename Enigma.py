from Plugboard import Plugboard
from Rotor import Rotor
import string

class Enigma():
    def __init__(self, rotor1, rotor2, rotor3, reflector, plugboard):
        self.__plugboard = plugboard
        self.__rotors = [rotor1, rotor2, rotor3]
        self.__reflector = reflector

    @property
    def rotors(self):
        return self.__rotors

    @property
    def reflector(self):
        return self.__reflector

    def encrypt(self, text):
        print(text)
        letters = []
        for letter in text:
            self.rotors[2].move_rotor()
            if self.rotors[2].if_notch():
                self.rotors[1].move_rotor()
            if self.rotors[1].if_notch():
                self.rotors[0].move_rotor()
            # TODO transition between keyboard and first rotor
            letter = self.__plugboard.encrypt_letter(letter)
            letter = self.rotor_transition(letter,  self.__plugboard, self.rotors[2])
            letter = self.rotors[2].encrypt_letter(letter)
            letter = self.rotor_transition(letter, self.rotors[2], self.rotors[1])
            letter = self.rotors[1].encrypt_letter(letter)
            letter = self.rotor_transition(letter, self.rotors[1], self.rotors[0])
            letter = self.rotors[0].encrypt_letter(letter)
            letter = self.rotor_transition(letter, self.rotors[0], self.reflector)
            letter = self.reflector.encrypt_letter(letter)
            letter = self.rotor_transition(letter, self.reflector,  self.rotors[0])
            letter = self.rotors[0].encrypt_letter2(letter)
            letter = self.rotor_transition(letter, self.rotors[0], self.rotors[1])
            letter = self.rotors[1].encrypt_letter2(letter)
            letter = self.rotor_transition(letter, self.rotors[1], self.rotors[2])
            letter = self.rotors[2].encrypt_letter2(letter)
            letter = self.rotor_transition(letter, self.rotors[2],  self.__plugboard)
            letters.append(letter)
            #print(letter)
        return ''.join(letters)


    @staticmethod
    def rotor_transition(letter, rotor1, rotor2):
        keys = string.ascii_uppercase
        shift1 = rotor1.shift
        shift2 = rotor2.shift

        let = Rotor.move_key(letter, shift2-shift1)
        #
        # which_a1 = rotor1_keys.index('A')
        # which_a2 = rotor2_keys.index('A')
        #
        # num = [x for x in rotor1_keys].index(letter)
        # let = [x for x in rotor2_keys][num-2*which_a1+2*which_a2]
        return let







