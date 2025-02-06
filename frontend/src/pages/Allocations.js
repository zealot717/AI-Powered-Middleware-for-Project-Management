import AllocationChart from "../components/AllocationChart";
import { useState, useEffect } from "react";
import api from "../services/api";

const Allocations = () => {
  const [allocations, setAllocations] = useState([]);

  useEffect(() => {
    api.get("/allocations").then((response) => {
      setAllocations(response.data);
    });
  }, []);

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-4">Resource Allocations</h2>
      <AllocationChart data={allocations} />
    </div>
  );
};

export default Allocations;
