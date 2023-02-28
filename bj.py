import random


class BJ:
    def __init__(self):
        self.count = 0

    def start(self):
        self.koloda = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4
        random.shuffle(self.koloda)
        current = self.koloda.pop()
        print('|', current, '|')
        self.count += current

    def take_a_card(self):
        while self.count < 21:
            current = self.koloda.pop()
            print('+', '|', current, '|')
            self.count += current
            if self.count > 21:
                print('Извините, но вы проиграли')
            elif self.count == 21:
                print('Поздравляю, вы набрали 21!')
            else:
                print('У вас %d очков.' %self.count)


new = BJ()
new.start()
new.take_a_card()
new.take_a_card()
new.take_a_card()
new.take_a_card()
new.take_a_card()