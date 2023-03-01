from flask import Flask, render_template
from flask import redirect, url_for, request
import random
app = Flask(__name__)




class BJ:
    def __init__(self):
        self.count = 0
        self.koloda = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4
        self.current = ''
        self.cards = {6 : '🂶 ', 7 : '🃇 ', 8 : '🃘 ', 9 : '🂩 ', 10 : '🃊 ', 2 : '🂻 ', 3 : '🂭 ', 4 :'🃞 ', 11 :'🃁 '}

    def start(self):
        self.count = 0
        self.koloda = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4
        self.current = ''
        random.shuffle(self.koloda)
        self.current = self.koloda.pop()
        self.count += self.current
        s = self.cards[self.current]
        self.to_print = []
        self.to_print.append(s)
        self.text = ''.join(self.to_print)
        self.start_message = 'У вас %d \n' % self.count
        return

    def take_a_card(self):
        while self.count < 21:
            self.current = self.koloda.pop()
            self.count += self.current
            ss = self.cards[self.current]
            self.to_print.append(ss)
            self.text = ''.join(self.to_print)
            return

    def winner(self):
        if self.count > 21:
            self.message = 'У вас %d \n' % self.count + 'Извините, но вы проиграли \n'
            return self.message
        elif self.count == 21:
            self.message = 'У вас 21 ! \n' + 'Поздравляю, вы победили! \n'
            return self.message
        else:
            self.message = 'У вас %d \n' % self.count
            return self.message


class Slots:

    def __init__(self):
        self.rand1 = 0
        self.rand2 = 0
        self.rand3 = 0

    def randomize(self):
        self.rand1 = random.randint(0, 6)
        self.rand2 = random.randint(0, 6)
        self.rand3 = random.randint(0, 6)

        if self.rand1 == self.rand2 == self.rand3:
            return str(self.rand1) + ' | ' + str(self.rand2) + ' | ' + str(self.rand3) + ' → ' + ' WIN!'
        else:
            return str(self.rand1) + ' | ' + str(self.rand2) + ' | ' + str(self.rand3) + ' → ' + ' LOSE'
        

my_game = BJ()

@app.route('/')
def main():
    return render_template('hub.html')


@app.route('/game1', methods=['GET', 'POST'])
def game1():
    if request.method == 'POST':
        if request.form.get('action1') == 'Start':
            my_game.start()
            return render_template('blackjack.html', data = my_game.text, message = my_game.start_message)
        elif request.form.get('action2') == 'Take a card':
            if my_game.count >= 21:
                return render_template('blackjack.html', data = my_game.text, message = 'Больше взять нельзя')
            else:
                my_game.take_a_card()
                my_game.winner()
                return render_template('blackjack.html', data =my_game.text, message = my_game.message)
        elif request.form.get('action3') == 'Return':
            return redirect('/game1')
        elif request.form.get('action4') == 'Stop':
            return redirect('/game1')
        elif request.form.get('action5') == 'Quit':
            return redirect('/')
        elif request.form.get('action6') == 'Again':
            my_game.start()
            return render_template('blackjack.html', data = my_game.text, message = my_game.start_message)


    elif request.method == 'GET':
        return render_template('game1.html')


@app.route('/hello')
def hello_casino():
    return render_template('hello.html', hello = '0 | 0 | 0')


@app.route('/game2')
def game2():
    slot = Slots()
    s = slot.randomize()
    return render_template('game2.html', data = str(s))    
    
    
    
if __name__ == '__main__':
    app.run(debug=True)
