import "./App.css";

function App() {
  return (
    <div className="app-container">
      {/* Header */}
      <header className="header">
        <div className="logo">🎮 Gaming Club</div>
        <nav className="nav">
          <button>Membership</button>
          <button>Member</button>
          <button>Add Game</button>
          <button>Collections</button>
        </nav>
        <div className="auth">
          <button>Admin</button>
          <button>Logout</button>
        </div>
      </header>

      {/* Main Section */}
      <main className="main-content">
        <h2>CREATE MEMBERSHIP</h2>
        <form className="form">
          <label>
            Name:
            <input type="text" placeholder="Enter name" />
          </label>
          <label>
            Phone:
            <input type="text" placeholder="Enter phone" />
          </label>
          <label>
            Membership Fee:
            <input type="number" placeholder="Enter fee" />
          </label>
          <button type="submit" className="submit-btn">
            Create Membership
          </button>
        </form>
      </main>

      {/* Footer */}
      <footer className="footer">
        © 2025 Gaming Club. All rights reserved.
      </footer>
    </div>
  );
}

export default App;