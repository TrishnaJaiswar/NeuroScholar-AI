import {
  Brain,
  Database,
  Network,
  FileSearch,
  ShieldCheck,
  Cpu,
} from "lucide-react";

const tech = [
  { icon: Brain, name: "LLMs", desc: "Groq + Llama 3.3" },
  { icon: Database, name: "Qdrant", desc: "Vector Database" },
  { icon: Network, name: "LangGraph", desc: "Agent Workflow" },
  { icon: FileSearch, name: "Advanced RAG", desc: "Hybrid Retrieval" },
  { icon: ShieldCheck, name: "Citation AI", desc: "Evidence Verification" },
  { icon: Cpu, name: "FastAPI", desc: "Backend API" },
];

export default function TechStack() {
  return (
    <section className="bg-white py-24 border-t">
      <div className="max-w-7xl mx-auto px-6">
        <div className="text-center">
          <span className="bg-blue-100 text-blue-700 px-4 py-2 rounded-full text-sm font-medium">
            Technology Stack
          </span>

          <h2 className="text-4xl font-bold mt-5 text-gray-900">
            Powered by Modern AI Infrastructure
          </h2>

          <p className="text-gray-600 mt-4 max-w-2xl mx-auto">
            Built with scalable technologies for intelligent document understanding
            and multi-agent reasoning.
          </p>
        </div>

        <div className="grid md:grid-cols-3 gap-6 mt-14">
          {tech.map((item, i) => {
            const Icon = item.icon;

            return (
              <div
                key={i}
                className="border border-gray-200 rounded-2xl p-6 hover:shadow-lg transition"
              >
                <div className="w-12 h-12 rounded-xl bg-blue-100 flex items-center justify-center mb-4">
                  <Icon className="text-blue-600" size={24} />
                </div>

                <h3 className="font-bold text-lg">{item.name}</h3>
                <p className="text-gray-500 mt-2">{item.desc}</p>
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
}