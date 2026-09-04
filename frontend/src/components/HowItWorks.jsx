import { Upload, Search, Brain, FileText } from "lucide-react";

const steps = [
  {
    icon: Upload,
    title: "Upload PDFs",
    desc: "Import one or multiple scientific papers into NeuroScholar.",
  },
  {
    icon: Search,
    title: "Hybrid Retrieval",
    desc: "Advanced RAG retrieves the most relevant evidence from documents.",
  },
  {
    icon: Brain,
    title: "Multi-Agent Analysis",
    desc: "Planner, Research, Analysis and Citation agents collaborate together.",
  },
  {
    icon: FileText,
    title: "Generate Report",
    desc: "Receive literature reviews, comparisons and citation-backed answers.",
  },
];

export default function HowItWorks() {
  return (
    <section className="bg-gray-50 py-24">
      <div className="max-w-6xl mx-auto px-6">
        <div className="text-center mb-16">
          <span className="bg-blue-100 text-blue-700 px-4 py-2 rounded-full text-sm font-medium">
            Workflow
          </span>

          <h2 className="text-4xl font-bold mt-5">
            How NeuroScholar AI Works
          </h2>

          <p className="text-gray-600 mt-4">
            From uploaded PDFs to evidence-grounded research reports.
          </p>
        </div>

        <div className="grid md:grid-cols-4 gap-8">
          {steps.map((step, index) => {
            const Icon = step.icon;

            return (
              <div key={index} className="relative text-center">
                <div className="w-16 h-16 rounded-full bg-blue-600 text-white flex items-center justify-center mx-auto">
                  <Icon size={28} />
                </div>

                <div className="absolute top-8 left-[60%] w-full h-[2px] bg-blue-200 hidden md:block last:hidden" />

                <h3 className="font-bold mt-6">{step.title}</h3>

                <p className="text-sm text-gray-600 mt-3 leading-6">
                  {step.desc}
                </p>
              </div>
            );
          })}
        </div>
      </div>
    </section>
  );
}