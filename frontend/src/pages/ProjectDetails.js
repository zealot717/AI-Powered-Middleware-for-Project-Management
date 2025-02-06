import React from "react";
import { useParams } from "react-router-dom";
import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import useFetch from "../hooks/useFetch";
import { API_BASE_URL } from "../services/api";

const ProjectDetails = () => {
  const { id } = useParams();
  const { data: project, loading } = useFetch(`${API_BASE_URL}/projects/${id}`);

  if (loading) return <p>Loading...</p>;

  return (
    <div className="flex">
      <Sidebar />
      <div className="flex-1 p-6">
        <Navbar />
        <h1 className="text-2xl font-bold mb-4">{project.name}</h1>
        <p><strong>Budget:</strong> ${project.budget}</p>
        <p><strong>Deadline:</strong> {project.deadline}</p>
        <p><strong>Risk Level:</strong> {project.riskLevel}</p>
        <h2 className="text-xl font-semibold mt-6">AI Recommendations</h2>
        <p>{project.aiRecommendation}</p>
      </div>
    </div>
  );
};

export default ProjectDetails;