import React from "react";
import "./Membership.css";

const Membership = () => {
  return (
    <div className="membership-container">
      <h2>CREATE MEMBERSHIP</h2>
      <form className="form" onSubmit={(e) => e.preventDefault()}>
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
        <button type="submit">Create Membership</button>
      </form>
    </div>
  );
};

export default Membership;
