import React, { useState } from "react";
import "./RephraserForm.css";

const RephraserForm = () => {
  const [text, setText] = useState("");
  const [tone, setTone] = useState("formal");
  const [output, setOutput] = useState("");
  const [loading, setLoading] = useState(false);
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);

  const toneOptions = [
    { value: "formal", label: "Formal", icon: "🎩", description: "Professional and polished" },
    { value: "informal", label: "Informal", icon: "😊", description: "Casual and relaxed" },
    { value: "concise", label: "Concise", icon: "⚡", description: "Brief and to the point" },
    { value: "friendly", label: "Friendly", icon: "🤝", description: "Warm and approachable" },
    { value: "creative", label: "Creative", icon: "🎨", description: "Imaginative and unique" }
  ];

  const selectedToneObj = toneOptions.find(opt => opt.value === tone);

  const handleRephrase = async () => {
    if (!text.trim()) return;

    setLoading(true);
    try {
      const response = await fetch("http://127.0.0.1:8000/smart_rephrase", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text, tone })
      });

      const data = await response.json();
      setOutput(data.final_output);
    } catch (error) {
      console.error("Error:", error);
      setOutput("Failed to rephrase. Please check if the backend is running.");
    } finally {
      setLoading(false);
    }
  };

  const handleCopy = () => {
    navigator.clipboard.writeText(output);
    alert("Copied to clipboard!");
  };

  const selectTone = (value) => {
    setTone(value);
    setIsDropdownOpen(false);
  };

  return (
    <section id="rephraser-section" className="rephraser-section">
      <div className="rephraser-container">
        <h2 className="section-title">Start Rephrasing</h2>

        {/* Input Area */}
        <div className="input-group">
          <label className="input-label">Your Text</label>
          <textarea
            className="text-input"
            placeholder="Paste or type your text here..."
            value={text}
            onChange={(e) => setText(e.target.value)}
          ></textarea>
          <div className="character-count">
            <span>{text.length} characters</span>
            {text.length > 0 && (
              <button className="clear-btn" onClick={() => setText("")}>
                Clear
              </button>
            )}
          </div>
        </div>

        {/* Style Dropdown */}
        <div className="style-group">
          <label className="input-label">Choose Style</label>
          <div className="dropdown-container">
            <button 
              className="dropdown-trigger"
              onClick={() => setIsDropdownOpen(!isDropdownOpen)}
            >
              <span className="selected-tone">
                <span className="tone-icon">{selectedToneObj.icon}</span>
                <span className="tone-info">
                  <span className="tone-name">{selectedToneObj.label}</span>
                  <span className="tone-desc">{selectedToneObj.description}</span>
                </span>
              </span>
              <span className={`dropdown-arrow ${isDropdownOpen ? 'open' : ''}`}>▼</span>
            </button>

            {isDropdownOpen && (
              <div className="dropdown-menu">
                {toneOptions.map((option) => (
                  <button
                    key={option.value}
                    className={`dropdown-item ${tone === option.value ? 'active' : ''}`}
                    onClick={() => selectTone(option.value)}
                  >
                    <span className="tone-icon">{option.icon}</span>
                    <span className="tone-info">
                      <span className="tone-name">{option.label}</span>
                      <span className="tone-desc">{option.description}</span>
                    </span>
                    {tone === option.value && <span className="checkmark">✓</span>}
                  </button>
                ))}
              </div>
            )}
          </div>
        </div>

        {/* Rephrase Button */}
        <button
          className={`rephrase-btn ${loading || !text.trim() ? 'disabled' : ''}`}
          onClick={handleRephrase}
          disabled={loading || !text.trim()}
        >
          {loading ? (
            <>
              <span className="spinner"></span>
              Processing...
            </>
          ) : (
            <>
              ✨ Rephrase Text
            </>
          )}
        </button>

        {/* Output Area */}
        {output && (
          <div className="output-section">
            <div className="output-header">
              <label className="input-label">Rephrased Result</label>
              <button className="copy-btn" onClick={handleCopy}>
                <svg className="copy-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
                </svg>
                Copy
              </button>
            </div>
            <div className="output-box">
              <p>{output}</p>
            </div>
          </div>
        )}
      </div>
    </section>
  );
};

export default RephraserForm;