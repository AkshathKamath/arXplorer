import "./App.css";
import { Routes, Route } from "react-router-dom";
import HomePage from "./views/Home";
import ViewPage from "./views/View";
import SummaryPage from "./views/Summarize";
import ScorePage from "./views/Score";
import ConnectPage from "./views/Connect";

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/home" element={<HomePage />} />
        <Route path="/view" element={<ViewPage />} />
        <Route path="/summarize" element={<SummaryPage />} />
        <Route path="/score" element={<ScorePage />} />
        <Route path="/connect" element={<ConnectPage />} />
      </Routes>
    </div>
  );
}

export default App;
