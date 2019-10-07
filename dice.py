import random

class Dice:
    def __init__(self, face_num):
        self.face_num = face_num 

    def shoot(self):
        return random.randint(1, self.face_num)
