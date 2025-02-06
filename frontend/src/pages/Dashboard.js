import React from "react";
import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import ProjectCard from "../components/ProjectCard";
import RiskCard from "../components/RiskCard";
import AllocationChart from "../components/AllocationChart";
import useFetch from "../hooks/useFetch";
import { API_BASE_URL } from "../services/api";

const Dashboard = () => {
  const { data: projects, loading, error } = useFetch(`${API_BASE_URL}/projects`);

  // Handle loading state
  if (loading) {
    return (
      <div className="flex">
        <Sidebar />
        <div className="flex-1 p-6">
          <Navbar />
          <p>Loading...</p>
        </div>
      </div>
    );
  }

  // Handle API errors
  if (error) {
    return (
      <div className="flex">
        <Sidebar />
        <div className="flex-1 p-6">
          <Navbar />
          <p className="text-red-500">Error loading projects. Please try again later.</p>
        </div>
      </div>
    );
  }

  // Ensure projects is an array before mapping
  const projectList = projects || [];

  return (
    <div className="flex">
      <Sidebar />
      <div className="flex-1 p-6">
        <Navbar />
        <h1 className="text-2xl font-bold mb-4">Dashboard</h1>

        {/* Projects Section */}
        {projectList.length > 0 ? (
          <div className="grid grid-cols-3 gap-4">
            {projectList.map((project) => (
              <ProjectCard key={project.id} project={project} />
            ))}
          </div>
        ) : (
          <p className="text-gray-500">No projects available.</p>
        )}

        {/* Risk Overview Section */}
        <div className="mt-6">
          <h2 className="text-xl font-semibold">Risk Overview</h2>
          {projectList.length > 0 ? (
            <div className="grid grid-cols-3 gap-4">
              {projectList.map((project) => (
                <RiskCard key={project.id} project={project} />
              ))}
            </div>
          ) : (
            <p className="text-gray-500">No risk data available.</p>
          )}
        </div>

        {/* Resource Allocation Section */}
        <div className="mt-6">
          <h2 className="text-xl font-semibold">Resource Allocation</h2>
          {projectList.length > 0 ? (
            <AllocationChart data={projectList} />
          ) : (
            <p className="text-gray-500">No allocation data available.</p>
          )}
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
