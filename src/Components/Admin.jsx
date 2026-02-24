import React, { useState } from "react";
import "./Admin.css";

function Admin() {
  const [activeTab, setActiveTab] = useState("searchMember");
  const [searchPhone, setSearchPhone] = useState("");
  const [newMember, setNewMember] = useState({ name: "", phone: "", fee: "" });
  const [newGame, setNewGame] = useState({ name: "", price: "", description: "" });
  const [message, setMessage] = useState("");

  // Dummy collection data
  const [collections] = useState([
    { member: "Suman", recharge: 50 },
    { member: "Sujan", recharge: 100 },
    { member: "Rakshith", recharge: 150 },
  ]);

  const handleSearch = () => {
    if (searchPhone) setMessage(`Searched for member: ${searchPhone}`);
    else setMessage("Please enter a phone number.");
  };

  const handleAddMember = () => {
    if (newMember.name && newMember.phone && newMember.fee)
      setMessage(`Added member: ${newMember.name}`);
    else setMessage("Please fill all member fields.");
  };

  const handleAddGame = () => {
    if (newGame.name && newGame.price && newGame.description)
      setMessage(`Added game: ${newGame.name}`);
    else setMessage("Please fill all game fields.");
  };

  const totalCollection = collections.reduce((acc, curr) => acc + curr.recharge, 0);

  return (
    <div className="admin-container">
      <h1>Admin Panel</h1>
      <div className="admin-tabs">
        <button
          className={activeTab === "searchMember" ? "active" : ""}
          onClick={() => setActiveTab("searchMember")}
        >
          Search Member
        </button>
        <button
          className={activeTab === "addMember" ? "active" : ""}
          onClick={() => setActiveTab("addMember")}
        >
          Add Membership
        </button>
        <button
          className={activeTab === "addGame" ? "active" : ""}
          onClick={() => setActiveTab("addGame")}
        >
          Add Game
        </button>
        <button
          className={activeTab === "collections" ? "active" : ""}
          onClick={() => setActiveTab("collections")}
        >
          Collections
        </button>
      </div>

      <div className="admin-content">
        {activeTab === "searchMember" && (
          <div className="tab-section">
            <h2>Search Member</h2>
            <input
              type="text"
              placeholder="Enter phone number"
              value={searchPhone}
              onChange={(e) => setSearchPhone(e.target.value)}
            />
            <button onClick={handleSearch}>Search</button>
          </div>
        )}

        {activeTab === "addMember" && (
          <div className="tab-section">
            <h2>Add Membership</h2>
            <input
              type="text"
              placeholder="Name"
              value={newMember.name}
              onChange={(e) => setNewMember({ ...newMember, name: e.target.value })}
            />
            <input
              type="text"
              placeholder="Phone"
              value={newMember.phone}
              onChange={(e) => setNewMember({ ...newMember, phone: e.target.value })}
            />
            <input
              type="number"
              placeholder="Membership Fee"
              value={newMember.fee}
              onChange={(e) => setNewMember({ ...newMember, fee: e.target.value })}
            />
            <button onClick={handleAddMember}>Add Member</button>
          </div>
        )}

        {activeTab === "addGame" && (
          <div className="tab-section">
            <h2>Add Game</h2>
            <input
              type="text"
              placeholder="Game Name"
              value={newGame.name}
              onChange={(e) => setNewGame({ ...newGame, name: e.target.value })}
            />
            <input
              type="number"
              placeholder="Price"
              value={newGame.price}
              onChange={(e) => setNewGame({ ...newGame, price: e.target.value })}
            />
            <input
              type="text"
              placeholder="Description"
              value={newGame.description}
              onChange={(e) => setNewGame({ ...newGame, description: e.target.value })}
            />
            <button onClick={handleAddGame}>Add Game</button>
          </div>
        )}

        {activeTab === "collections" && (
          <div className="tab-section">
            <h2>Collections</h2>
            <table>
              <thead>
                <tr>
                  <th>Member</th>
                  <th>Recharge Amount</th>
                </tr>
              </thead>
              <tbody>
                {collections.map((c, idx) => (
                  <tr key={idx}>
                    <td>{c.member}</td>
                    <td>₹{c.recharge}</td>
                  </tr>
                ))}
              </tbody>
              <tfoot>
                <tr>
                  <td>Total</td>
                  <td>₹{totalCollection}</td>
                </tr>
              </tfoot>
            </table>
          </div>
        )}
      </div>

      {message && <div className="admin-message">{message}</div>}
    </div>
  );
}

export default Admin;
