from flask import Flask, render_template
from flask import redirect, url_for, request
import random
app = Flask(__name__)




class BJ:
    def __init__(self):
        self.count = 0
        self.koloda = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4
        self.current = ''
        self.cards = {6 : '<font size="100px">🂶</font>', 7 : '<font size="100px">🃇</font>', 8 : '<font size="100px">🃘</font>', 9 : '<font size="100px">🂩</font>', 10 : '<font size="100px">🃊</font>', 2 : '<font size="100px">🂻</font>', 3 : '<font size="100px">🂭</font>', 4 :'<font size="100px">🃞</font>', 11 :'<font size="100px">🃁</font>'}

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
        s = ''.join(self.to_print)
        return s

    def take_a_card(self):
        while self.count < 21:
            self.current = self.koloda.pop()
            self.count += self.current
            ss = self.cards[self.current]
            self.to_print.append(ss)
            ss = ''.join(self.to_print)
            return ss

    def winner(self):
        if self.count > 21:
            return('<br>У вас %d очков.' % self.count + '<br>Извините, но вы проиграли' + '<form method="post" action="/game1" ><input type="submit" value="Again" name="action6" /></form>' + '<form method="post" action="/game1" ><input type="submit" value="Return" name="action3" /></form>')
        elif self.count == 21:
            return('<br>У вас 21 очко!.' + '<br>Поздравляю, вы набрали 21!' + '<form method="post" action="/game1" ><input type="submit" value="Again" name="action6" /></form>' + '<form method="post" action="/game1" ><input type="submit" value="Return" name="action3" /></form>')
        else:
            return('<br>У вас %d очков.' % self.count + '<form method="post" action="/game1" ><input type="submit" value="Take a card" name="action2" /></form>' + '<form method="post" action="/game1" ><input type="submit" value="Stop" name="action4" /></form>')


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
            return str(self.rand1) + ' | ' + str(self.rand2) + ' | ' + str(self.rand3) + ' --> ' + ' WIN!'
        else:
            return str(self.rand1) + ' | ' + str(self.rand2) + ' | ' + str(self.rand3) + ' --> ' + ' LOSE'
        

my_game = BJ()

@app.route('/')
def main():
    return render_template('hub.html')


@app.route('/game1', methods=['GET', 'POST'])
def game1():
    if request.method == 'POST':
        if request.form.get('action1') == 'Start':
            my_game.start()
            return my_game.start() + '<form method="post" action="/game1" ><input type="submit" value="Take a card" name="action2" /></form>'
        elif request.form.get('action2') == 'Take a card':
            my_game.winner()
            return my_game.take_a_card() + str(my_game.winner())
        elif request.form.get('action3') == 'Return':
            return redirect('/game1')
        elif request.form.get('action4') == 'Stop':
            return redirect('/game1')
        elif request.form.get('action5') == 'Quit':
            return redirect('/')
        elif request.form.get('action6') == 'Again':
            my_game.start()
            return my_game.start() + '<form method="post" action="/game1" ><input type="submit" value="Take a card" name="action2" /></form>'


    elif request.method == 'GET':
        return render_template('game1.html')


@app.route('/slots')
def hello_casino():
    return render_template('slots.html', hello = str(0) + '|' + str(0) + '|' + str(0))


@app.route('/game2')
def game2():
    slot = Slots()
    s = slot.randomize()
    return render_template('game2.html', data = str(s))    
    
    
    
if __name__ == '__main__':
    app.run(debug=True)
