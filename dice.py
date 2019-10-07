import random

class Dice:
    def __init__(self, face_num=6):
        self.face_num = face_num 

    def shoot(self):
        return random.randint(1, self.face_num)
