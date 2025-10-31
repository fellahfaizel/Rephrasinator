import React from "react";
import "./Header.css";

const Header = () => {
  const scrollToForm = () => {
    document.getElementById("rephraser-section").scrollIntoView({ 
      behavior: "smooth" 
    });
  };

  return (
    <header className="header-container">
      <div className="header-content">
        <div className="header-left">
          <h1 className="app-title">
            Rephrasinator
          </h1>
          <div className="title-underline"></div>
        </div>
        
        <div className="header-right">
          <div className="description-box">
            <h2 className="description-title">Transform Your Text Instantly</h2>
            <p className="description-text">
              Rephrasinator is an AI-powered tool that helps you rewrite and 
              enhance your text with different styles and tones. Whether you need 
              formal business communication, friendly messages, or concise summaries, 
              our intelligent system provides grammatically perfect rephrased content 
              in seconds.
            </p>
            <button className="start-button" onClick={scrollToForm}>
              Let's Start
              <span className="arrow">→</span>
            </button>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;