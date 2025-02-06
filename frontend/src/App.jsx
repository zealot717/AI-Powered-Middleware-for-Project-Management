import React from "react";
import { Routes, Route } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import Projects from "./pages/Projects";
import ProjectDetails from "./pages/ProjectDetails";
import AIAnalysis from "./pages/AIAnalysis";
import RiskAnalysis from "./pages/RiskAnalysis";
import Allocations from "./pages/Allocations";
import Navbar from "./components/Navbar";
import Sidebar from "./components/Sidebar";
import "./index.css";

function App() {
  return (
    <div className="flex h-screen bg-gray-100">
      <Sidebar />
      <div className="flex flex-col flex-1">
        <Navbar />
        <main className="p-6">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/projects" element={<Projects />} />
            <Route path="/projects/:id" element={<ProjectDetails />} />
            <Route path="/ai-analysis" element={<AIAnalysis />} />
            <Route path="/risk-analysis" element={<RiskAnalysis />} />
            <Route path="/allocations" element={<Allocations />} />
          </Routes>
        </main>
      </div>
    </div>
  );
}

export default App;
