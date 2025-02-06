import React from "react";
import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import ProjectCard from "../components/ProjectCard";
import RiskCard from "../components/RiskCard";
import AllocationChart from "../components/AllocationChart";
import useFetch from "../hooks/useFetch";
import { API_BASE_URL } from "../services/api";

const Dashboard = () => {
  const { data: projects, loading, error } = useFetch("/projects");

  if (loading) return <p className="text-center text-gray-500">Loading...</p>;
  if (error) return <p className="text-center text-red-500">Error loading projects. Please try again.</p>;

  return (
    <div className="flex h-screen">
      <Sidebar />
      <div className="flex-1 p-6 bg-gray-50">
        <Navbar />
        <h1 className="text-3xl font-bold mb-6">Dashboard</h1>

        {/* Projects Section */}
        <section>
          <h2 className="text-xl font-semibold mb-2">Projects</h2>
          <div className="grid grid-cols-3 gap-4">
            {projects.length > 0 ? (
              projects.map((project) => <ProjectCard key={project.id} project={project} />)
            ) : (
              <p className="text-gray-500">No projects available.</p>
            )}
          </div>
        </section>

        {/* Risk Overview */}
        <section className="mt-6">
          <h2 className="text-xl font-semibold">Risk Overview</h2>
          <div className="grid grid-cols-3 gap-4">
            {projects.length > 0 ? (
              projects.map((project) => <RiskCard key={project.id} project={project} />)
            ) : (
              <p className="text-gray-500">No risk data available.</p>
            )}
          </div>
        </section>

        {/* Resource Allocation */}
        <section className="mt-6">
          <h2 className="text-xl font-semibold">Resource Allocation</h2>
          <AllocationChart data={projects} />
        </section>
      </div>
    </div>
  );
};

export default Dashboard;
