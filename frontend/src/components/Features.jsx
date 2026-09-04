import { useNavigate, Link } from "react-router-dom";
import { useChatStore } from "../store/chatStore";
import {
  MessageSquare,
  BookOpen,
  GitCompare,
  TrendingUp,
  ArrowRight,
  ShieldCheck,
  Search,
  Database,
} from "lucide-react";

const features = [
  {
    icon: MessageSquare,
    title: "Research Chat",
    task: "qa",
    desc: "Ask natural language questions across multiple research papers using Advanced RAG.",
    color: "bg-blue-100 text-blue-600",
  },
  {
    icon: BookOpen,
    title: "Literature Review",
    task: "literature_review",
    desc: "Generate structured academic literature reviews with citations and key findings.",
    color: "bg-indigo-100 text-indigo-600",
  },
  {
    icon: GitCompare,
    title: "Compare Papers",
    task: "compare_papers",
    desc: "Compare methodology, datasets, architecture and results side-by-side.",
    color: "bg-cyan-100 text-cyan-600",
  },
  {
    icon: TrendingUp,
    title: "Trend Analysis",
    task: "trend_analysis",
    desc: "Identify emerging topics and research trends from scientific publications.",
    color: "bg-sky-100 text-sky-600",
  },
  {
    icon: Search,
    title: "Hybrid Retrieval",
    task: "qa",
    desc: "Semantic + BM25 search with reranking for highly relevant document retrieval.",
    color: "bg-blue-100 text-blue-600",
  },
  {
    icon: ShieldCheck,
    title: "Citation Verification",
    task: "qa",
    desc: "Every important claim is grounded with evidence from retrieved papers.",
    color: "bg-indigo-100 text-indigo-600",
  },
  {
    icon: Database,
    title: "PDF Knowledge Base",
    task: "qa",
    desc: "Upload and index research papers into your personal scientific knowledge base.",
    color: "bg-cyan-100 text-cyan-600",
  },
];

export default function Features() {
  const navigate = useNavigate();
  const setActiveTask = useChatStore((state) => state.setActiveTask);

  const openDashboard = (task) => {
    setActiveTask(task);
    navigate("/dashboard");
  };

  return (
    <section className="bg-gray-50 py-24">
      <div className="max-w-7xl mx-auto px-6">
        {/* Header */}
        <div className="text-center max-w-3xl mx-auto">
          <span className="bg-blue-100 text-blue-700 px-4 py-2 rounded-full text-sm font-medium">
            Platform Features
          </span>

          <h2 className="text-5xl font-bold text-gray-900 mt-6">
            Everything You Need For Scientific Research
          </h2>

          <p className="text-gray-600 text-lg leading-8 mt-6">
            NeuroScholar AI combines Advanced RAG, Multi-Agent AI and citation
            verification into one intelligent research workspace.
          </p>
        </div>

        {/* Cards */}
        <div className="grid md:grid-cols-2 xl:grid-cols-3 gap-8 mt-16">
          {features.map((feature, index) => {
            const Icon = feature.icon;

            return (
              <div
                key={index}
                className="bg-white rounded-3xl border border-gray-200 p-7 hover:shadow-xl hover:-translate-y-1 transition duration-300 flex flex-col"
              >
                <div
                  className={`w-14 h-14 rounded-2xl flex items-center justify-center ${feature.color}`}
                >
                  <Icon size={28} />
                </div>

                <h3 className="text-2xl font-bold text-gray-900 mt-6">
                  {feature.title}
                </h3>

                <p className="text-gray-600 leading-7 mt-3 flex-1">
                  {feature.desc}
                </p>

                <button
                  onClick={() => openDashboard(feature.task)}
                  className="mt-6 inline-flex items-center gap-2 text-blue-600 font-semibold hover:text-blue-700"
                >
                  Open Dashboard
                  <ArrowRight size={18} />
                </button>
              </div>
            );
          })}
        </div>

        {/* CTA */}
        <div className="mt-24 bg-blue-600 rounded-3xl p-12 text-center text-white">
          <h3 className="text-4xl font-bold">
            Ready to accelerate your research?
          </h3>

          <p className="text-blue-100 mt-4 text-lg">
            Upload PDFs, ask questions and generate research reports in minutes.
          </p>

          <button
            onClick={() => openDashboard("qa")}
            className="inline-block mt-8 bg-white text-blue-600 px-8 py-3 rounded-xl font-semibold hover:bg-gray-100 transition"
          >
            Launch NeuroScholar AI
          </button>
        </div>
      </div>
    </section>
  );
}