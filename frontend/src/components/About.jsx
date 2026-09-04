import { Brain, Search, FileCheck, GitBranch } from "lucide-react";

const features = [
  {
    icon: Brain,
    title: "Multi-Agent AI",
    desc: "Planner, Retrieval, Research, Analysis, Critic and Citation agents collaborate to solve complex research tasks.",
  },
  {
    icon: Search,
    title: "Advanced RAG",
    desc: "Hybrid search, reranking and metadata-aware retrieval provide accurate, evidence-grounded answers.",
  },
  {
    icon: FileCheck,
    title: "Citation Verification",
    desc: "Every important claim is linked back to supporting research papers for trustworthy outputs.",
  },
  {
    icon: GitBranch,
    title: "LangGraph Workflow",
    desc: "Conditional routing enables QA, literature review, paper comparison and trend analysis in one system.",
  },
];

export default function About() {
  return (
    <section className="bg-white py-24">
      <div className="max-w-7xl mx-auto px-6">
        {/* Heading */}
        <div className="text-center max-w-3xl mx-auto">
          <span className="bg-blue-100 text-blue-700 px-4 py-2 rounded-full text-sm font-medium">
            About NeuroScholar AI
          </span>

          <h2 className="text-5xl font-bold text-gray-900 mt-6">
            Built for Researchers, Students & Engineers
          </h2>

          <p className="text-gray-600 text-lg leading-8 mt-6">
            NeuroScholar AI is an intelligent research assistant that combines
            Large Language Models, Advanced Retrieval-Augmented Generation,
            LangGraph orchestration and evidence-based citation verification into
            one seamless platform.
          </p>
        </div>

        {/* Cards */}
        <div className="grid md:grid-cols-2 gap-8 mt-16">
          {features.map((item, index) => {
            const Icon = item.icon;

            return (
              <div
                key={index}
                className="border border-gray-200 rounded-3xl p-8 hover:shadow-xl transition duration-300"
              >
                <div className="w-14 h-14 rounded-2xl bg-blue-100 flex items-center justify-center mb-6">
                  <Icon className="text-blue-600" size={28} />
                </div>

                <h3 className="text-2xl font-bold text-gray-900 mb-3">
                  {item.title}
                </h3>

                <p className="text-gray-600 leading-7">{item.desc}</p>
              </div>
            );
          })}
        </div>

        {/* Mission */}
        <div className="mt-20 bg-blue-600 rounded-3xl p-10 text-white">
          <h3 className="text-3xl font-bold mb-4">Our Mission</h3>

          <p className="text-blue-100 leading-8 text-lg max-w-4xl">
            Make scientific research faster, more reliable and accessible through
            AI-powered workflows that generate literature reviews, compare papers,
            answer technical questions and verify every response with citations.
          </p>
        </div>
      </div>
    </section>
  );
}