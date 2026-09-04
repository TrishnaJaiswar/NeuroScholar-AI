import { Upload, Download } from "lucide-react";

export default function Topbar() {
  return (
    <header className="h-16 border-b border-gray-200 px-6 flex items-center justify-between bg-white">
      <div>
        <h2 className="font-bold text-lg text-gray-900">
          Research Chat
        </h2>
        <p className="text-xs text-gray-500">
          Advanced RAG • Multi-Agent Workflow
        </p>
      </div>

      <div className="flex gap-3">
        <button className="border border-gray-300 rounded-lg px-4 py-2 text-sm flex items-center gap-2">
          <Upload size={16} />
          Upload
        </button>

        <button className="bg-blue-600 hover:bg-blue-700 text-white rounded-lg px-4 py-2 text-sm flex items-center gap-2">
          <Download size={16} />
          Export
        </button>
      </div>
    </header>
  );
}