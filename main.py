from Enigma import Enigma
from Rotor import Rotor
from Reflector import Reflector
from Plugboard import Plugboard
import string

if __name__ == '__main__':
    map = {1: 5, 2: 4, 3: 6}
    #rotor = Rotor(int_map=string.ascii_uppercase, notch='Q')
    rotor1 = Rotor(let_map="I")
    rotor2 = Rotor(let_map='II')
    rotor3 = Rotor(let_map='III')
    reflector = Reflector(let_map="B")
    plugboard = Plugboard(let_map='empty')
    enigma = Enigma(rotor1, rotor2, rotor3, reflector, plugboard)
    text = input("Podaj tekst do zakodowania:")
    x = enigma.encrypt(text)
    print(x)

    # letter = 'H'
    # x = rotor3.encrypt_letter(letter)
    # print(x)
    # rotor3.move_rotor()
    # x = rotor3.encrypt_letter(letter)
    # print(x)
    # x = reflector.encrypt_letter(letter)
    # print(x)

