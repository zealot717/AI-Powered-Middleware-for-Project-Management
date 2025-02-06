import React from "react";
import { Bar } from "recharts";

const AllocationChart = ({ data }) => {
  return (
    <div className="p-4 bg-white shadow-md rounded-md">
      <h2 className="text-lg font-semibold mb-2">Resource Allocation</h2>
      <Bar data={data} />
    </div>
  );
};

export default AllocationChart;