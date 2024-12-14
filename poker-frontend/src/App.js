import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [gameState, setGameState] = useState(null);
  const [message, setMessage] = useState("");

  // Fetch game state on load
  useEffect(() => {
    fetchGameState();
  }, []);

  const fetchGameState = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:8000/state");
      setGameState(response.data.game_state);
    } catch (error) {
      console.error("Error fetching game state:", error);
    }
  };

  const handleAction = async (action) => {
    try {
      const response = await axios.post("http://127.0.0.1:8000/action", {
        action,
      });
      setMessage(response.data.message);
      setGameState(response.data.game_state);
    } catch (error) {
      console.error("Error performing action:", error);
    }
  };

  if (!gameState) return <div>Loading...</div>;

  return (
      <div>
        <h1>Poker Game</h1>
        <pre>{JSON.stringify(gameState, null, 2)}</pre>
        <p>{message}</p>
        <div>
          <button onClick={() => handleAction("Call")}>Call</button>
          <button onClick={() => handleAction("Raise:50")}>Raise 50</button>
          <button onClick={() => handleAction("Fold")}>Fold</button>
        </div>
      </div>
  );
}

export default App;
