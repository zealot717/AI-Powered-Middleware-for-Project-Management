import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav className="bg-gray-900 text-white p-4 flex justify-between items-center">
      <h1 className="text-xl font-bold">Aerospace Project Manager</h1>
      <div>
        <Link to="/" className="mx-4 hover:text-gray-400">Dashboard</Link>
        <Link to="/projects" className="mx-4 hover:text-gray-400">Projects</Link>
        <Link to="/ai-analysis" className="mx-4 hover:text-gray-400">AI Analysis</Link>
        <Link to="/risk-analysis" className="mx-4 hover:text-gray-400">Risk Analysis</Link>
        <Link to="/allocations" className="mx-4 hover:text-gray-400">Allocations</Link>
      </div>
    </nav>
  );
};

export default Navbar;
