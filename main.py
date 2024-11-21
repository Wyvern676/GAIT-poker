from app import gameLogic, aiLogic, imageGeneration, textToSpeech, musicGeneration

def main():
    print("Welcome to Poker Game!")
    # Initialize game logic
    game = game_logic.PokerGame()
    # Setup AI opponent
    opponent = ai_logic.create_opponent("Old Western Cowboy")
    # Start game
    game.start(opponent)

if __name__ == "__main__":
    main()
