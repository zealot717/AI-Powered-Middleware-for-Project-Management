/*import axios from "axios";

export const API_BASE_URL = "http://localhost:8000/api"; // Ensure this matches backend

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

export const fetchProjects = async () => {
  try {
    const response = await api.get("/projects");
    return response.data;
  } catch (error) {
    console.error("Error fetching projects:", error);
    return [];
  }
};

export const fetchOptimizedResources = async (projectId) => {
  try {
    const response = await api.get(`/get_optimized_resources/${projectId}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching optimized resources:", error);
    return null;
  }
};

export const fetchRiskAssessment = async (projectId) => {
  try {
    const response = await api.get(`/get_risk_assessment/${projectId}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching risk assessment:", error);
    return null;
  }
};

export const triggerOptimization = async (projectId) => {
  try {
    const response = await api.post(`/run_optimization/${projectId}`);
    return response.data;
  } catch (error) {
    console.error("Error triggering optimization:", error);
    return null;
  }
};

export const triggerRiskAssessment = async (projectId) => {
  try {
    const response = await api.post(`/run_risk_assessment/${projectId}`);
    return response.data;
  } catch (error) {
    console.error("Error triggering risk assessment:", error);
    return null;
  }
};

export default api;*/
import axios from "axios";

const API_BASE_URL = "http://localhost:8000/api"; // Ensure the correct format

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

export { API_BASE_URL }; // Export this to use elsewhere
export default api;
