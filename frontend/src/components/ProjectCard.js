import { Link } from "react-router-dom";

const ProjectCard = ({ project }) => {
  return (
    <div className="bg-white shadow-lg rounded-lg p-4 m-2">
      <h3 className="text-xl font-bold mb-2">{project.name}</h3>
      <p className="text-gray-600">Budget: ${project.budget}</p>
      <p className="text-gray-600">Deadline: {project.deadline}</p>
      <p className={`text-sm font-semibold ${project.riskLevel === 'High' ? 'text-red-600' : 'text-green-600'}`}>
        Risk Level: {project.riskLevel}
      </p>
      <Link to={`/projects/${project.id}`} className="block mt-4 text-blue-500 hover:underline">
        View Details
      </Link>
    </div>
  );
};

export default ProjectCard;
