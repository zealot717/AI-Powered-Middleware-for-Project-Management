import React, { useEffect, useState } from "react";
import { fetchProjects } from "../services/api";
import { Link } from "react-router-dom";

const Dashboard = () => {
    const [projects, setProjects] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const loadProjects = async () => {
            try {
                const data = await fetchProjects();
                setProjects(data);
            } catch (err) {
                setError("Failed to fetch projects");
            } finally {
                setLoading(false);
            }
        };

        loadProjects();
    }, []);

    if (loading) return <p>Loading projects...</p>;
    if (error) return <p>{error}</p>;

    return (
        <div className="p-4">
            <h1 className="text-xl font-bold mb-4">Project Dashboard</h1>
            <ul className="space-y-3">
                {projects.map((project) => (
                    <li key={project.ProjectID} className="p-2 bg-gray-100 rounded">
                        <Link to={`/project/${project.ProjectID}`} className="text-blue-500">
                            {project.ProjectName} ({project.Status})
                        </Link>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Dashboard;
