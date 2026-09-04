import { Link, NavLink } from "react-router-dom";

export default function Navbar() {
  const linkClass = ({ isActive }) =>
    isActive
      ? "text-blue-600 font-semibold"
      : "text-gray-700 hover:text-blue-600";

  return (
    <nav className="sticky top-0 z-50 bg-white/90 backdrop-blur border-b border-gray-200">
      <div className="max-w-7xl mx-auto h-16 px-6 flex items-center justify-between">
        <Link to="/" className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-xl bg-blue-600 text-white flex items-center justify-center font-bold">
            N
          </div>
          <div>
            <h1 className="font-bold text-lg">NeuroScholar AI</h1>
            <p className="text-xs text-gray-500">Research Platform</p>
          </div>
        </Link>

        <div className="flex items-center gap-8 text-sm">
          <NavLink to="/" className={linkClass}>Home</NavLink>
          <NavLink to="/about" className={linkClass}>About</NavLink>
          <NavLink to="/features" className={linkClass}>Features</NavLink>

          <Link
            to="/dashboard"
            className="bg-blue-600 hover:bg-blue-700 text-white px-5 py-2 rounded-lg font-medium transition"
          >
            Launch App
          </Link>
        </div>
      </div>
    </nav>
  );
}