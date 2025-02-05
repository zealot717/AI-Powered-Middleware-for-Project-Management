const API_BASE_URL = "http://localhost:8000";

export const fetchProjects = async () => {
    const response = await fetch(`${API_BASE_URL}/projects`);
    return response.json();
};

export const fetchProjectDetails = async (id) => {
    const response = await fetch(`${API_BASE_URL}/projects/${id}`);
    return response.json();
};

export const fetchResources = async () => {
    const response = await fetch(`${API_BASE_URL}/resources`);
    return response.json();
};

export const fetchRiskAnalysis = async () => {
    const response = await fetch(`${API_BASE_URL}/risk-analysis`);
    return response.json();
};
