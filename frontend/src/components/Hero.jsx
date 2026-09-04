import { Link } from "react-router-dom";
import { ArrowRight, FileText, Brain, Search } from "lucide-react";

export default function Hero() {
  return (
    <section className="bg-white">
      <div className="max-w-7xl mx-auto px-6 py-24 grid lg:grid-cols-2 gap-16 items-center">

        {/* Left */}
        <div>
          <span className="inline-flex items-center gap-2 bg-blue-100 text-blue-700 px-4 py-2 rounded-full text-sm font-medium">
            <Brain size={16} />
            Multi-Agent Research Platform
          </span>

          <h1 className="text-6xl font-bold text-gray-900 leading-tight mt-6">
            Read, Compare & Generate Research Faster
          </h1>

          <p className="text-gray-600 text-lg leading-8 mt-6">
            NeuroScholar AI helps students and researchers analyze scientific
            papers using Advanced RAG, LangGraph orchestration and citation verification.
          </p>

          <div className="flex gap-4 mt-10">
            <Link
              to="/dashboard"
              className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-xl flex items-center gap-2 font-medium transition"
            >
              Launch Dashboard
              <ArrowRight size={18} />
            </Link>

            <Link
              to="/features"
              className="border border-gray-300 hover:border-blue-600 px-6 py-3 rounded-xl font-medium transition"
            >
              Explore Features
            </Link>
          </div>

          {/* Stats */}
          <div className="grid grid-cols-3 gap-6 mt-14">
            <div>
              <h3 className="text-3xl font-bold">10+</h3>
              <p className="text-gray-500 text-sm">AI Agents</p>
            </div>

            <div>
              <h3 className="text-3xl font-bold">RAG</h3>
              <p className="text-gray-500 text-sm">Hybrid Search</p>
            </div>

            <div>
              <h3 className="text-3xl font-bold">100%</h3>
              <p className="text-gray-500 text-sm">Citation Based</p>
            </div>
          </div>
        </div>

        {/* Right */}
        <div className="bg-gray-50 rounded-3xl border border-gray-200 shadow-xl p-6">

          {/* User Question */}
          <div className="bg-white rounded-2xl border p-4">
            <div className="flex items-center gap-2 text-sm text-gray-500 mb-3">
              <Search size={16} />
              User Query
            </div>

            <div className="bg-blue-600 text-white rounded-xl p-3">
              Compare BERT vs GPT for NLP tasks
            </div>
          </div>

          {/* AI Response */}
          <div className="bg-white rounded-2xl border p-5 mt-5">
            <div className="flex items-center gap-2 mb-3">
              <Brain className="text-blue-600" size={18} />
              <p className="font-semibold">NeuroScholar AI</p>
            </div>

            <h3 className="font-bold text-lg mb-2">
              Comparative Analysis
            </h3>

            <p className="text-gray-600 text-sm leading-7">
              BERT is an encoder-based Transformer optimized for language
              understanding, while GPT is a decoder-based model specialized
              for text generation and reasoning.
            </p>

            <div className="flex gap-2 mt-5">
              <span className="bg-green-100 text-green-700 px-3 py-1 rounded-full text-xs">
                Verified
              </span>

              <span className="bg-blue-100 text-blue-700 px-3 py-1 rounded-full text-xs">
                Citation Included
              </span>
            </div>
          </div>

          {/* Mini Cards */}
          <div className="grid grid-cols-2 gap-4 mt-5">

            <div className="bg-white rounded-xl border p-4">
              <FileText className="text-blue-600 mb-2" />
              <h4 className="font-semibold text-sm">Literature Review</h4>
              <p className="text-xs text-gray-500 mt-1">
                Auto-generated reports
              </p>
            </div>

            <div className="bg-white rounded-xl border p-4">
              <Brain className="text-blue-600 mb-2" />
              <h4 className="font-semibold text-sm">Multi-Agent</h4>
              <p className="text-xs text-gray-500 mt-1">
                Planner → Citation
              </p>
            </div>

          </div>

        </div>
      </div>
    </section>
  );
}