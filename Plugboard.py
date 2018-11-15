from Reflector import Reflector
import string


class Plugboard(Reflector):
    maps_preset = {'empty': string.ascii_uppercase}

    def __init__(self, let_map):
        super().__init__(let_map)
