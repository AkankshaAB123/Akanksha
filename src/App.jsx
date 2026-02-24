import React from "react";
import { Routes, Route } from "react-router-dom";
import "./App.css";

import Header from "./Components/Header.jsx";
import Footer from "./Components/Footer.jsx";
import Home from "./Components/Home.jsx";
import Login from "./Components/Login.jsx";
import Signup from "./Components/Signup.jsx";
import Admin from "./Components/Admin.jsx";
import Membership from "./Components/Membership.jsx";
import MemberSearch from "./Components/MemberSearch.jsx";
import MemberPage from "./Components/MemberPage.jsx";
import AddGame from "./Components/AddGame.jsx";
import Collections from "./Components/Collections.jsx";
import PlayGame from "./Components/PlayGame.jsx";

function App() {
  return (
    <div className="app-container">
      <Header />

      <main className="main-content">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/admin" element={<Admin />} />
          <Route path="/membership" element={<Membership />} />
          <Route path="/member-search" element={<MemberSearch />} />
          <Route path="/member-page" element={<MemberPage />} />
          <Route path="/add-game" element={<AddGame />} />
          <Route path="/collections" element={<Collections />} />
          <Route path="/play-game" element={<PlayGame />} />
        </Routes>
      </main>

      <Footer />
    </div>
  );
}

export default App;
