import React, { useState } from "react";
import "./Collections.css";


const Collections = () => {
  const [date, setDate] = useState("");

  const collectionsData = [
    { member: "Suman", amount: 50 },
    { member: "Sujan", amount: 100 },
    { member: "Rakshith", amount: 150 },
  ];

  const total = collectionsData.reduce((sum, item) => sum + item.amount, 0);

  const handleSearch = (e) => {
    e.preventDefault();
    alert(`Showing collections for date: ${date || "All Dates"}`);
  };

  return (
    <div className="collections-container">
      <h2>RECHARGE COLLECTIONS</h2>
      <form className="date-form" onSubmit={handleSearch}>
        <label>
          Date:
          <input type="date" value={date} onChange={(e) => setDate(e.target.value)} />
        </label>
        <button type="submit">Search</button>
      </form>

      <table>
        <thead>
          <tr>
            <th>Member</th>
            <th>Recharge</th>
          </tr>
        </thead>
        <tbody>
          {collectionsData.map((item, index) => (
            <tr key={index}>
              <td>{item.member}</td>
              <td>₹{item.amount}</td>
            </tr>
          ))}
        </tbody>
        <tfoot>
          <tr>
            <td>Total</td>
            <td>₹{total}</td>
          </tr>
        </tfoot>
      </table>
    </div>
  );
};

export default Collections;
