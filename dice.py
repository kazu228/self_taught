import random

class Dice:
    def __init__(self, face_num=6):
        if face_num not in [4,6,8,12,20]:
            raise Exception('そんな正多面体はありません。')
        self.face_num = face_num 

    def shoot(self):
        return random.randint(1, self.face_num)

a = Dice()
print(a.shoot())