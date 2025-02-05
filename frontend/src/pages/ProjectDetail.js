import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { fetchProjectDetails } from "../services/api";

const ProjectDetail = () => {
    const { id } = useParams();
    const [project, setProject] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const loadProjectDetails = async () => {
            try {
                const data = await fetchProjectDetails(id);
                setProject(data);
            } catch (err) {
                setError("Failed to fetch project details");
            } finally {
                setLoading(false);
            }
        };

        loadProjectDetails();
    }, [id]);

    if (loading) return <p>Loading project details...</p>;
    if (error) return <p>{error}</p>;

    return (
        <div className="p-4">
            <h1 className="text-xl font-bold mb-4">{project.ProjectName}</h1>
            <p><strong>Status:</strong> {project.Status}</p>
            <p><strong>Start Date:</strong> {project.StartDate}</p>
            <p><strong>End Date:</strong> {project.EndDate}</p>
            <p><strong>Budget:</strong> ${project.Budget.toLocaleString()}</p>

            <h2 className="text-lg font-bold mt-4">Tasks</h2>
            <ul className="space-y-3">
                {project.Tasks.map((task) => (
                    <li key={task.TaskID} className="p-2 bg-gray-100 rounded">
                        <p><strong>{task.TaskName}</strong></p>
                        <p>{task.StartDate} → {task.EndDate}</p>
                    </li>
                ))}
            </ul>

            <h2 className="text-lg font-bold mt-4">Allocated Resources</h2>
            <ul className="space-y-3">
                {project.AllocatedResources.map((resource) => (
                    <li key={resource.ResourceID} className="p-2 bg-gray-100 rounded">
                        <p><strong>{resource.Name}</strong> - {resource.Role}</p>
                        <p>Availability: {resource.Availability}%</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ProjectDetail;
