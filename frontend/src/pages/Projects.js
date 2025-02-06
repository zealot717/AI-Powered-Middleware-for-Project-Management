import React from "react";
import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import Table from "../components/Table";
import useFetch from "../hooks/useFetch";
import { API_BASE_URL } from "../services/api";

const Projects = () => {
  const { data: projects, loading } = useFetch(`${API_BASE_URL}/projects`);

  if (loading) return <p>Loading...</p>;

  const headers = ["Name", "Budget", "Deadline", "Risk Level"];
  const data = projects.map((proj) => ({
    Name: proj.name,
    Budget: `$${proj.budget}`,
    Deadline: proj.deadline,
    "Risk Level": proj.riskLevel,
  }));

  return (
    <div className="flex">
      <Sidebar />
      <div className="flex-1 p-6">
        <Navbar />
        <h1 className="text-2xl font-bold mb-4">Projects</h1>
        <Table headers={headers} data={data} />
      </div>
    </div>
  );
};

export default Projects;
