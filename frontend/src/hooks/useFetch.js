/*import { useState, useEffect } from "react";
import axios from "axios";
import { API_BASE_URL } from "../services/api";

const useFetch = (endpoint) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(`${API_BASE_URL}${endpoint}`);
        setData(response.data);
      } catch (err) {
        console.error("API fetch error:", err);
        setError(err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [endpoint]);

  return { data, loading, error };
};

export default useFetch;*/
import { useState, useEffect } from "react";
import api, { API_BASE_URL } from "../services/api";

const useFetch = (endpoint) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await api.get(endpoint); // Ensure correct endpoint format
        setData(response.data);
      } catch (err) {
        console.error("API fetch error:", err);
        setError("Error loading data. Please try again later.");
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, [endpoint]);

  return { data, loading, error };
};

export default useFetch;

