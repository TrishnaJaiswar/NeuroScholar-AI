import { Link } from "react-router-dom";

export default function Footer() {
  return (
    <footer className="bg-gray-50 border-t border-gray-200 mt-20">
      <div className="max-w-7xl mx-auto px-6 py-12">
        <div className="grid md:grid-cols-3 gap-10">
          {/* Brand */}
          <div>
            <h2 className="text-2xl font-bold text-gray-900">
              NeuroScholar AI
            </h2>
            <p className="text-gray-600 mt-3 leading-7">
              AI-powered scientific research platform built with React, FastAPI,
              LangGraph and Advanced RAG.
            </p>

            <div className="mt-5">
              <p className="text-sm font-semibold text-gray-800">
                Developed by Trishna Jaiswar
              </p>
              <a
                href="https://github.com/YOUR_GITHUB_USERNAME"
                target="_blank"
                rel="noreferrer"
                className="text-blue-600 text-sm hover:underline"
              >
                GitHub Profile
              </a>
              <br></br>
              <a
                href="https://www.linkedin.com/in/trishna-jaiswar-404409257E"
                target="_blank"
                rel="noreferrer"
                className="text-blue-600 text-sm hover:underline"
              >
                Linkedin Profile
              </a>
            </div>
          </div>

          {/* Navigation */}
          <div>
            <h3 className="font-semibold text-gray-900 mb-4">Navigation</h3>

            <div className="space-y-3 text-gray-600">
              <Link to="/" className="block hover:text-blue-600">Home</Link>
              <Link to="/about" className="block hover:text-blue-600">About</Link>
              <Link to="/features" className="block hover:text-blue-600">Features</Link>
              <Link to="/dashboard" className="block hover:text-blue-600">Dashboard</Link>
            </div>
          </div>

          {/* Features */}
          <div>
            <h3 className="font-semibold text-gray-900 mb-4">Features</h3>

            <div className="space-y-3 text-gray-600 text-sm">
              <p>Research Chat</p>
              <p>Literature Review</p>
              <p>Compare Papers</p>
              <p>Trend Analysis</p>
              <p>Citation Verification</p>
            </div>
          </div>
        </div>

        <div className="border-t border-gray-200 mt-10 pt-6 flex flex-col md:flex-row justify-between items-center text-sm text-gray-500">
          <p>© 2026 NeuroScholar AI. All rights reserved.</p>

          <p className="mt-3 md:mt-0">
            Built with ❤️ by Trishna Jaiswar
          </p>
        </div>
      </div>
    </footer>
  );
}