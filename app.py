import os

from flask import Flask, request, render_template, jsonify
from poker_game import PokerGame, Deck

app = Flask(__name__)
print("Current working directory:", os.getcwd())
# Initialize game state
game = PokerGame()

@app.route('/')
def index():
    print("Current working directory:", os.getcwd())
    # Render the game UI with the current game state
    return render_template('game.html', game_state=game.get_gamestate())

@app.route('/action', methods=['POST'])
def player_action():
    # Handle player actions (Call, Raise, Fold)
    action = request.json['action']
    if action == "Call":
        result = game.call_bet()
    elif action.startswith("Raise"):
        amount = int(action.split(":")[1])
        result = game.raise_bet(amount)
    elif action == "Fold":
        result = game.fold_hand()
    else:
        result = "Invalid action."

    # Update the game state and return the result
    return jsonify({
        "message": result,
        "game_state": game.get_gamestate()
    })

if __name__ == '__main__':
    app.run(debug=True)
