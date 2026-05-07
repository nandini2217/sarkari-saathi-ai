import React, { useState, useRef } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [query, setQuery] = useState("");
  const [answer, setAnswer] = useState("");
  const [audio, setAudio] = useState(null);
  const [loading, setLoading] = useState(false);
  const [recording, setRecording] = useState(false);

  const mediaRecorderRef = useRef(null);
  const audioChunksRef = useRef([]);

  // ✅ TEXT QUERY
  const handleAsk = async () => {
    if (!query.trim()) return;

    setLoading(true);
    setAnswer("");
    setAudio(null);

    try {
      const res = await axios.get(
        `http://127.0.0.1:8000/api/v1/rag/ask?query=${query}`
      );

      setAnswer(res.data.answer);
    } catch (err) {
      console.error(err);
      setAnswer("❌ Error fetching response");
    }

    setLoading(false);
  };

  // ✅ START RECORDING
  const startRecording = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({
        audio: true,
      });

      const mediaRecorder = new MediaRecorder(stream);

      mediaRecorderRef.current = mediaRecorder;
      audioChunksRef.current = [];

      mediaRecorder.ondataavailable = (event) => {
        audioChunksRef.current.push(event.data);
      };

      mediaRecorder.onstop = async () => {
        const audioBlob = new Blob(audioChunksRef.current, {
          type: "audio/wav",
        });

        const audioFile = new File(
          [audioBlob],
          "voice.wav",
          { type: "audio/wav" }
        );

        const formData = new FormData();
        formData.append("file", audioFile);

        setLoading(true);
        setAnswer("🎤 Processing voice...");
        setAudio(null);

        try {
          const res = await axios.post(
            "http://127.0.0.1:8000/api/v1/voice/ask",
            formData,
            {
              headers: {
                "Content-Type": "multipart/form-data",
              },
            }
          );

          setAnswer(res.data.answer);

          setAudio(
            `http://127.0.0.1:8000/static/${res.data.audio_file}`
          );
        } catch (err) {
          console.error(err);
          setAnswer("❌ Voice processing error");
        }

        setLoading(false);
      };

      mediaRecorder.start();
      setRecording(true);

    } catch (err) {
      console.error(err);
      alert("Microphone access denied");
    }
  };

  // ✅ STOP RECORDING
  const stopRecording = () => {
    mediaRecorderRef.current.stop();
    setRecording(false);
  };

  return (
    <div className="container">
      <h1 className="title">🇮🇳 Sarkari Saathi AI</h1>

      <input
        type="text"
        placeholder="Ask about government schemes..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        className="input-box"
      />

      <div className="button-group">
        <button
          className="btn"
          onClick={handleAsk}
          disabled={loading}
        >
          {loading ? "Loading..." : "Ask"}
        </button>

        {!recording ? (
          <button
            className="btn"
            onClick={startRecording}
            disabled={loading}
          >
            🎤 Start Speaking
          </button>
        ) : (
          <button
            className="btn"
            onClick={stopRecording}
          >
            ⏹ Stop Recording
          </button>
        )}
      </div>

      <div className="answer-box">
        <h3>Answer:</h3>

        <p>{answer}</p>

        {audio && (
          <audio controls autoPlay>
            <source src={audio} type="audio/mp3" />
          </audio>
        )}
      </div>
    </div>
  );
}

export default App;