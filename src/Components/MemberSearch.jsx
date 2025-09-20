import React, { useState } from "react";
import "./MemberSearch.css";

const MemberSearch = () => {
  const [phone, setPhone] = useState("");

  const handleSearch = (e) => {
    e.preventDefault();
    alert(`Searching member with phone: ${phone}`);
  };

  return (
    <div className="member-search-container">
      <h2>MEMBER SEARCH</h2>
      <form onSubmit={handleSearch} className="search-form">
        <label>
          Phone:
          <input
            type="text"
            placeholder="Enter phone"
            value={phone}
            onChange={(e) => setPhone(e.target.value)}
          />
        </label>
        <button type="submit">Search</button>
      </form>
    </div>
  );
};

export default MemberSearch;
