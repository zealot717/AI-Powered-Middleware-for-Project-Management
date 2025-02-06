import { Link } from "react-router-dom";

const Sidebar = () => {
  return (
    <aside className="bg-gray-800 text-white w-64 min-h-screen p-5">
      <h2 className="text-lg font-bold mb-4">Navigation</h2>
      <ul>
        <li className="mb-2">
          <Link to="/" className="block py-2 px-4 hover:bg-gray-700 rounded">Dashboard</Link>
        </li>
        <li className="mb-2">
          <Link to="/projects" className="block py-2 px-4 hover:bg-gray-700 rounded">Projects</Link>
        </li>
        <li className="mb-2">
          <Link to="/ai-analysis" className="block py-2 px-4 hover:bg-gray-700 rounded">AI Analysis</Link>
        </li>
        <li className="mb-2">
          <Link to="/risk-analysis" className="block py-2 px-4 hover:bg-gray-700 rounded">Risk Analysis</Link>
        </li>
        <li>
          <Link to="/allocations" className="block py-2 px-4 hover:bg-gray-700 rounded">Allocations</Link>
        </li>
      </ul>
    </aside>
  );
};

export default Sidebar;
