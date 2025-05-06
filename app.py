from flask import Flask, render_template, redirect, url_for
from playsound import playsound
from game import TicTacToe
import threading

app = Flask(__name__)
game = TicTacToe()

def play_sound_async(path):
    threading.Thread(target=playsound, args=(path,), daemon=True).start()

@app.route("/")
def index():
    return render_template(
        "index.html",
        board=game.board,
        winner=game.winner,
        current_player=game.current_player,
        tie=game.tie
    )

@app.route("/move/<int:position>")
def move(position):
    if game.game_running and game.board[position] == "-":
        game.make_move(position)
        play_sound_async("static/click.wav")

        if game.game_running:
            game.computer_move()
            play_sound_async("static/click.wav")

        if game.winner:
            play_sound_async("static/win.wav")
        elif game.tie:
            play_sound_async("static/tie.mp3")

    return redirect(url_for("index"))

@app.route("/reset")
def reset():
    global game
    game = TicTacToe()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
