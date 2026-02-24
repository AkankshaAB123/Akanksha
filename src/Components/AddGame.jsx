import React, { useState } from "react";
import "./AddGame.css";

const AddGame = () => {
  const [name, setName] = useState("");
  const [price, setPrice] = useState("");
  const [description, setDescription] = useState("");
  const [minPlayers, setMinPlayers] = useState("");
  const [multipleAllowed, setMultipleAllowed] = useState(false);

  const handleAddGame = (e) => {
    e.preventDefault();
    alert(`Game Added:\nName: ${name}\nPrice: ₹${price}\nDescription: ${description}`);
    // Reset form
    setName("");
    setPrice("");
    setDescription("");
    setMinPlayers("");
    setMultipleAllowed(false);
  };

  return (
    <div className="add-game-container">
      <h2>ADD GAME</h2>
      <form onSubmit={handleAddGame} className="form">
        <label>
          Game Name:
          <input type="text" value={name} onChange={(e) => setName(e.target.value)} placeholder="Enter game name" />
        </label>

        <label>
          Price (₹):
          <input type="number" value={price} onChange={(e) => setPrice(e.target.value)} placeholder="Enter price" />
        </label>

        <label>
          Description:
          <input type="text" value={description} onChange={(e) => setDescription(e.target.value)} placeholder="Enter description" />
        </label>

        <label>
          Min Players:
          <input type="number" value={minPlayers} onChange={(e) => setMinPlayers(e.target.value)} placeholder="Min players" />
        </label>

        <label>
          Multiple Allowed:
          <input type="checkbox" checked={multipleAllowed} onChange={(e) => setMultipleAllowed(e.target.checked)} />
        </label>

        <button type="submit">Add Game</button>
      </form>
    </div>
  );
};

export default AddGame;
