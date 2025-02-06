import React from "react";
import { Link } from "react-router-dom";
import useFetch from "../hooks/useFetch";

const Projects = () => {
  const { data: projects, loading, error } = useFetch("/projects");

  if (loading) return <p className="text-gray-500">Loading projects...</p>;
  if (error) return <p className="text-red-500">Error loading projects.</p>;

  return (
    <div className="p-6">
      <h1 className="text-3xl font-bold mb-6">Projects</h1>
      {projects.length > 0 ? (
        <table className="min-w-full bg-white border border-gray-300 shadow-lg rounded-lg">
          <thead className="bg-gray-100">
            <tr>
              <th className="py-2 border">Name</th>
              <th className="py-2 border">Budget</th>
              <th className="py-2 border">Deadline</th>
              <th className="py-2 border">Status</th>
              <th className="py-2 border">Action</th>
            </tr>
          </thead>
          <tbody>
            {projects.map((project) => (
              <tr key={project.project_id} className="border text-center">
                <td className="py-2 px-4">{project.project_name}</td>
                <td className="py-2 px-4">${project.budget.toLocaleString()}</td>
                <td className="py-2 px-4">{project.end_date}</td>
                <td className="py-2 px-4">{project.status}</td>
                <td className="py-2 px-4">
                  <Link to={`/projects/${project.project_id}`} className="text-blue-500 hover:underline">
                    View Details
                  </Link>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p className="text-gray-500 text-center">No projects available.</p>
      )}
    </div>
  );
};

export default Projects;
  