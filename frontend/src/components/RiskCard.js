import React from "react";

const RiskCard = ({ project }) => {
  return (
    <div className="bg-red-100 border-l-4 border-red-500 text-red-700 p-4 rounded-md">
      <p className="font-semibold">{project.name}</p>
      <p>Risk Level: {project.riskLevel}</p>
    </div>
  );
};

export default RiskCard;