# app.py

from flask import Flask, render_template, request, redirect, url_for, session
from game import Minesweeper

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required to use sessions securely

@app.route('/')
def index():
    # If no game in session, create a new one
    if 'game' not in session:
        session['game'] = Minesweeper(8, 8, 10).to_dict()
    
    # Load game from session
    game = Minesweeper.from_dict(session['game'])

    return render_template(
        'index.html',
        board=game.board,
        revealed=game.revealed,
        game_over=game.game_over,
        win=game.win
    )

@app.route('/click/<int:row>/<int:col>', methods=['POST'])
def click(row, col):
    game = Minesweeper.from_dict(session['game'])
    game.reveal(row, col)
    session['game'] = game.to_dict()
    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    session.pop('game', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
