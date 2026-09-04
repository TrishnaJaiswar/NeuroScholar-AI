import { useChatStore } from "../store/chatStore";
import { CheckCircle2, FileText } from "lucide-react";

export default function Workspace() {
  const selectedDocuments = useChatStore(
    (state) => state.selectedDocuments
  );

  const activeTask = useChatStore((state) => state.activeTask);

  const agents = [
    "Planner Agent",
    "Retrieval Agent",
    "Research Agent",
    "Analysis Agent",
    "Citation Agent",
    "Report Agent",
  ];

  const progress = {
    qa: 4,
    literature_review: 8,
    compare_papers: 8,
    trend_analysis: 8,
  };

  return (
    <aside className="w-80 border-l border-gray-200 bg-white p-5 overflow-y-auto">
      <h3 className="font-bold text-lg mb-4 text-gray-900">
        Workspace
      </h3>

      {/* Selected PDFs */}
      <div className="border rounded-2xl p-4 mb-5">
        <div className="flex items-center justify-between mb-3">
          <span className="font-semibold text-sm">
            Selected PDFs
          </span>

          <span className="text-xs text-emerald-600">
            {selectedDocuments.length} Selected
          </span>
        </div>

        <div className="space-y-2 max-h-36 overflow-y-auto">
          {selectedDocuments.length === 0 ? (
            <div className="h-24 rounded-xl bg-gray-100 flex items-center justify-center text-gray-400 text-sm">
              No PDF Selected
            </div>
          ) : (
            selectedDocuments.map((doc, i) => (
              <div
                key={i}
                className="flex items-center gap-2 rounded-lg bg-gray-50 border p-2"
              >
                <FileText size={16} className="text-blue-600" />
                <span className="text-sm truncate">{doc}</span>
              </div>
            ))
          )}
        </div>
      </div>

      {/* Agents */}
      <h4 className="font-semibold text-sm text-gray-700 mb-3">
        Active Agents
      </h4>

      <div className="space-y-3">
        {agents.map((agent) => (
          <div
            key={agent}
            className="border rounded-xl p-3 flex items-start justify-between gap-3"
          >
            <span className="text-sm font-medium text-gray-700 leading-tight break-words flex-1">
              {agent}
            </span>

            <CheckCircle2
              size={18}
              className="text-emerald-600 shrink-0 mt-0.5"
            />
          </div>
        ))}
      </div>

      {/* Progress */}
      <div className="mt-6 border rounded-xl p-4 bg-blue-50">
        <p className="text-sm font-semibold text-blue-700">
          Retrieval Progress
        </p>

        <div className="w-full h-2 bg-white rounded-full mt-3">
          <div
            className="h-2 bg-blue-600 rounded-full"
            style={{
              width: `${(progress[activeTask] / 10) * 100}%`,
            }}
          />
        </div>

        <p className="text-xs text-gray-600 mt-2">
          {progress[activeTask]} chunks retrieved
        </p>
      </div>
    </aside>
  );
}