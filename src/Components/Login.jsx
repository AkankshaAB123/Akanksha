import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Login.css";

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleLogin = (e) => {
    e.preventDefault();
    if (username && password) {
      // Redirect to membership page (or any other page)
      navigate("/membership");
    } else {
      alert("Please enter username and password");
    }
  };

  return (
    <div className="login-container">
      <h1>GAMING CLUB APP</h1>
      <form onSubmit={handleLogin} className="login-form">
        <label>
          Username:
          <input
            type="text"
            placeholder="Enter username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </label>

        <label>
          Password:
          <input
            type="password"
            placeholder="Enter password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </label>

        <button type="submit">Login</button>
      </form>

      <footer className="login-footer">
        © 2025 Gaming Club. All rights reserved.
      </footer>
    </div>
  );
};

export default Login;
