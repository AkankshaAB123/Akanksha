import React, { useState } from "react";
import "./PlayGame.css";

function PlayGame() {
  const [selectedGame, setSelectedGame] = useState("");
  const [message, setMessage] = useState("");

  const games = ["Chess", "Carrom", "Ludo", "PUBG", "Call of Duty"];

  const handlePlay = () => {
    if (selectedGame) {
      setMessage(`🎮 You started playing ${selectedGame}! Enjoy the game!`);
    } else {
      setMessage("⚠️ Please select a game first.");
    }
  };

  return (
    <div className="playgame-container">
      <h1>Play a Game</h1>
      <p>Select a game from the list and click Play.</p>

      <div className="game-select">
        <select
          value={selectedGame}
          onChange={(e) => setSelectedGame(e.target.value)}
        >
          <option value="">-- Choose a Game --</option>
          {games.map((game, index) => (
            <option key={index} value={game}>
              {game}
            </option>
          ))}
        </select>

        <button onClick={handlePlay}>Play</button>
      </div>

      {message && <div className="game-message">{message}</div>}
    </div>
  );
}

export default PlayGame;
