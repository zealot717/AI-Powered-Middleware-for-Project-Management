import React, { useEffect, useState } from "react";
import { fetchResources } from "../services/api";

const ResourceView = () => {
    const [resources, setResources] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const loadResources = async () => {
            try {
                const data = await fetchResources();
                setResources(data);
            } catch (err) {
                setError("Failed to fetch resources");
            } finally {
                setLoading(false);
            }
        };

        loadResources();
    }, []);

    if (loading) return <p>Loading resources...</p>;
    if (error) return <p>{error}</p>;

    return (
        <div className="p-4">
            <h1 className="text-xl font-bold mb-4">Resource Allocation</h1>
            <ul className="space-y-3">
                {resources.map((resource) => (
                    <li key={resource.ResourceID} className="p-2 bg-gray-100 rounded">
                        <p><strong>{resource.Name}</strong> - {resource.Role}</p>
                        <p>Availability: {resource.Availability}%</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ResourceView;
