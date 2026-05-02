import { useState } from "react";
import axios from "axios";
import "./App.css";
import { useRef, useEffect } from "react";

function App() {
  const [file, setFile] = useState(null);
  const [chatMsg, setChatMsg] = useState("");
  const [messages, setMessages] = useState([]);
  const [jobs, setJobs] = useState([]);

  const API = "http://127.0.0.1:8000";

  const [typing, setTyping] = useState(false);
  const chatEndRef = useRef(null);
  const uploadResume = async () => {
    const formData = new FormData();
    formData.append("file", file);
    formData.append("user_id", "harsh123");

    await axios.post(`${API}/upload-resume`, formData);
    alert("Resume uploaded!");
  };

  const getRecommendations = async () => {
    const formData = new FormData();
    formData.append("file", file);

    const res = await axios.post(`${API}/recommend-jobs`, formData);
    setJobs(res.data.recommended_jobs);
  };

  const typeMessage = (text, callback) => {
    let i = 0;
    let current = "";

    const interval = setInterval(() => {
      current += text[i];
      callback(current);
      i++;

      if (i >= text.length) {
        clearInterval(interval);
      }
    }, 15); // speed control
  };

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const chat = async () => {
    if (!chatMsg) return;

    const userMessage = chatMsg;

    setMessages((prev) => [
      ...prev,
      { role: "user", text: userMessage },
    ]);

    setChatMsg("");
    setTyping(true);

    const formData = new FormData();
    formData.append("user_id", "harsh123");
    formData.append("message", userMessage);

    const res = await axios.post(`${API}/chat`, formData);

    setTyping(false);

    // add empty AI message first
    setMessages((prev) => [
      ...prev,
      { role: "ai", text: "" }
    ]);

    // animate typing
    typeMessage(res.data.reply, (typedText) => {
      setMessages((prev) => {
        const updated = [...prev];
        updated[updated.length - 1].text = typedText;
        return updated;
      });
    });
  };

  return (
    <div className="container">
      <div className="title">AI Resume Analyzer</div>

      {/* Upload */}
      <div className="card">
        <input
          type="file"
          onChange={(e) => setFile(e.target.files[0])}
        />
        <br /><br />
        <button className="button" onClick={uploadResume}>
          Upload Resume
        </button>
        <button className="button button-green" onClick={getRecommendations}>
          Recommend Jobs
        </button>
      </div>

      {/* Jobs */}
      <div className="card">
        <h3>Job Recommendations</h3>
        {jobs.map((job, i) => (
          <div key={i} className="job-card">
            {job.job_role} — {job.score}%
          </div>
        ))}
      </div>

      {/* Chat */}
      <div className="card">
        <h3>Chat with AI</h3>

        <div className="chat-container">
          <div className="chat-box">
            {messages.map((msg, i) => (
              <div key={i} className={`message ${msg.role}`}>
                <div className="bubble">{msg.text}</div>
              </div>
            ))}

            {typing && <div className="typing">AI is thinking...</div>}

            <div ref={chatEndRef}></div>
          </div>

          <div className="chat-input">
            <input
              value={chatMsg}
              onChange={(e) => setChatMsg(e.target.value)}
              placeholder="Type your message..."
              onKeyDown={(e) => e.key === "Enter" && chat()}
            />

            <button onClick={chat} disabled={typing}>
              {typing ? "..." : "Send"}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;