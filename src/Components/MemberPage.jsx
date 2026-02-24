import React, { useState } from "react";
import "./MemberPage.css";

const MemberPage = () => {
  const [activeTab, setActiveTab] = useState("games");

  return (
    <div className="member-page-container">
      <h2>MEMBER DETAILS</h2>
      <div className="member-info">
        <p><strong>Name:</strong> John Doe</p>
        <p><strong>Phone:</strong> 9876543210</p>
        <p><strong>Balance:</strong> ₹500</p>
      </div>

      <div className="tabs">
        <button
          className={activeTab === "games" ? "active" : ""}
          onClick={() => setActiveTab("games")}
        >
          Games
        </button>
        <button
          className={activeTab === "recharge" ? "active" : ""}
          onClick={() => setActiveTab("recharge")}
        >
          Recharge History
        </button>
        <button
          className={activeTab === "played" ? "active" : ""}
          onClick={() => setActiveTab("played")}
        >
          Played Games
        </button>
      </div>

      <div className="tab-content">
        {activeTab === "games" && (
          <table>
            <thead>
              <tr>
                <th>Name</th>
                <th>Price</th>
                <th>Description</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Chess</td>
                <td>₹50</td>
                <td>2 players needed</td>
                <td><button>Play Game</button></td>
              </tr>
              <tr>
                <td>Carrom</td>
                <td>₹100</td>
                <td>2–4 players</td>
                <td><button>Play Game</button></td>
              </tr>
              <tr>
                <td>Foosball</td>
                <td>₹150</td>
                <td>Multiple allowed</td>
                <td><button>Play Game</button></td>
              </tr>
            </tbody>
          </table>
        )}

        {activeTab === "recharge" && (
          <table>
            <thead>
              <tr>
                <th>Date/Time</th>
                <th>Amount</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>2025-09-05 11:30</td>
                <td>₹200</td>
              </tr>
              <tr>
                <td>2025-09-02 15:10</td>
                <td>₹300</td>
              </tr>
            </tbody>
          </table>
        )}

        {activeTab === "played" && (
          <table>
            <thead>
              <tr>
                <th>Date/Time</th>
                <th>Game</th>
                <th>Amount</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>2025-09-06 19:45</td>
                <td>Chess</td>
                <td>₹50</td>
              </tr>
              <tr>
                <td>2025-09-05 18:20</td>
                <td>Carrom</td>
                <td>₹100</td>
              </tr>
              <tr>
                <td>2025-09-02 16:00</td>
                <td>Foosball</td>
                <td>₹150</td>
              </tr>
            </tbody>
          </table>
        )}
      </div>
    </div>
  );
};

export default MemberPage;
