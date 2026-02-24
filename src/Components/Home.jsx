import React from "react";
import "./Home.css";

const Home = () => {
  return (
    <div className="home-container">
      <h1>🎮 Welcome to Gaming Club App</h1>
      <p>
        Join our gaming community and enjoy a variety of games, membership perks,
        and track your played games & recharges easily!
      </p>
      <div className="home-buttons">
        <button onClick={() => alert("Navigate to Login")}>Login</button>
        <button onClick={() => alert("Navigate to Signup")}>Create Account</button>
      </div>
      <div className="home-footer">
        © 2025 Gaming Club. All rights reserved.
      </div>
    </div>
  );
};

export default Home;
