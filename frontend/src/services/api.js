import axios from "axios";

export const API_BASE_URL = "http://localhost:8000/api"; // Ensure correct API base URL

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

export const fetchAIAnalysis = async () => {
  try {
    const response = await api.get("/ai-analysis");
    return response.data;
  } catch (error) {
    console.error("Error fetching AI analysis:", error);
    return { optimizedAllocations: [], riskPrediction: "No data" };
  }
};

export const fetchRiskAnalysis = async () => {
  try {
    const response = await api.get("/risk-analysis");
    return response.data;
  } catch (error) {
    console.error("Error fetching risk analysis:", error);
    return [];
  }
};
export const fetchAllocations = async () => {
  try {
    const response = await api.get("/allocations");
    return response.data;
  } catch (error) {
    console.error("Error fetching allocations:", error);
    return [];
  }
};


export default api;


