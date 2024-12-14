from fastapi import FastAPI
from pydantic import BaseModel
from gameLogic import PokerGame

app = FastAPI()
game = PokerGame()  # Initialize the game globally

class ActionRequest(BaseModel):
    action: str

@app.get("/state")
def get_state():
    """Return the current game state."""
    return {"game_state": game.get_gamestate()}

@app.post("/action")
def take_action(request: ActionRequest):
    """Process player action (Call, Raise, Fold)."""
    action = request.action
    if action == "Call":
        result = game.call_bet()
    elif action.startswith("Raise"):
        amount = int(action.split(":")[1])
        result = game.raise_bet(amount)
    elif action == "Fold":
        result = game.fold_hand()
    else:
        result = "Invalid action."

    return {"message": result, "game_state": game.get_gamestate()}
