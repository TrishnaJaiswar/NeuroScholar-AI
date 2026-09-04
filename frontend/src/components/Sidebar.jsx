import { useRef, useState, useEffect } from "react";
import api from "../services/api";
import { useChatStore } from "../store/chatStore";
import {
  MessageSquare,
  BookOpen,
  Files,
  TrendingUp,
  FolderOpen,
  Plus,
  History,
} from "lucide-react";

const menu = [
  { icon: MessageSquare, name: "Research Chat", task: "qa" },
  { icon: BookOpen, name: "Literature Review", task: "literature_review" },
  { icon: Files, name: "Compare Papers", task: "compare_papers" },
  { icon: TrendingUp, name: "Trend Analysis", task: "trend_analysis" },
];

export default function Sidebar() {
  const fileInputRef = useRef();

  const [documents, setDocuments] = useState([]);
  const [sessions, setSessions] = useState([]);

  const {
    activeTask,
    setActiveTask,
    selectedDocuments,
    toggleDocument,
    replaceMessages,
    setCurrentSession,
    clearCurrentChat,
  } = useChatStore();

  const loadDocuments = async () => {
    const res = await api.get("/documents");
    setDocuments(res.data);
  };

  const loadSessions = async () => {
    const res = await api.get("/sessions");
    setSessions(res.data.reverse());
  };

  useEffect(() => {
    loadDocuments();
    loadSessions();
  }, []);

  const handleUpload = async (e) => {
    const pdf = e.target.files[0];
    if (!pdf) return;

    const form = new FormData();
    form.append("file", pdf);

    await api.post("/upload", form);

    loadDocuments();
  };

  const openSession = async (id) => {
    const res = await api.get(`/sessions/${id}`);

    setActiveTask(res.data.task);
    replaceMessages(res.data.messages);
    setCurrentSession(id);
  };

  return (
    <aside className="w-64 border-r bg-white p-5 flex flex-col">
      {/* Logo */}
      <div className="flex items-center gap-3 mb-8">
        <div className="h-11 w-11 rounded-xl bg-blue-600 text-white flex items-center justify-center font-bold">
          N
        </div>

        <div>
          <h1 className="font-bold">NeuroScholar</h1>
          <p className="text-xs text-gray-500">
            AI Research Platform
          </p>
        </div>
      </div>

      {/* Upload */}
      <input
        ref={fileInputRef}
        type="file"
        accept=".pdf"
        className="hidden"
        onChange={handleUpload}
      />

      <button
        onClick={() => fileInputRef.current.click()}
        className="bg-blue-600 text-white rounded-xl py-3 flex items-center justify-center gap-2 mb-3"
      >
        <Plus size={18} />
        Upload PDF
      </button>

      {/* New Chat */}
      <button
        onClick={() => {
          clearCurrentChat();
          setCurrentSession(null);
        }}
        className="border rounded-xl py-3 flex items-center justify-center gap-2 mb-6 hover:bg-gray-50"
      >
        <MessageSquare size={18} />
        New Chat
      </button>

      {/* Workflows */}
      <nav className="space-y-1">
        {menu.map((item) => (
          <button
            key={item.task}
            onClick={() => setActiveTask(item.task)}
            className={`w-full flex items-center gap-3 px-3 py-3 rounded-lg ${
              activeTask === item.task
                ? "bg-blue-50 text-blue-700"
                : "hover:bg-gray-100"
            }`}
          >
            <item.icon size={18} />
            {item.name}
          </button>
        ))}
      </nav>

      {/* PDF Library */}
      <div className="mt-6">
        <div className="flex items-center gap-2 mb-3">
          <FolderOpen size={16} />
          <h3 className="text-sm font-semibold">
            PDF Library
          </h3>
        </div>

        <div className="space-y-2 max-h-40 overflow-y-auto">
          {documents.map((doc, i) => (
            <label
              key={i}
              className="flex gap-2 text-sm border rounded p-2 cursor-pointer hover:bg-gray-50"
            >
              <input
                type="checkbox"
                checked={selectedDocuments.includes(doc.name)}
                onChange={() => toggleDocument(doc.name)}
              />
              <span className="truncate">{doc.name}</span>
            </label>
          ))}
        </div>
      </div>

      {/* Saved Sessions */}
      <div className="mt-6">
        <div className="flex items-center gap-2 mb-3">
          <History size={16} />
          <h3 className="text-sm font-semibold">
            Research History
          </h3>
        </div>

        <div className="space-y-2 max-h-44 overflow-y-auto">
          {sessions.map((s) => (
            <button
              key={s.id}
              onClick={() => openSession(s.id)}
              className="w-full text-left border rounded-lg p-2 hover:bg-gray-50"
            >
              <p className="text-sm font-medium truncate">
                {s.title}
              </p>

              <p className="text-xs text-gray-500">
                {s.task.replace("_", " ")}
              </p>
            </button>
          ))}
        </div>
      </div>

      {/* Status */}
      <div className="mt-auto border rounded-xl p-3 bg-gray-50">
        <p className="font-semibold text-sm">FastAPI</p>
        <p className="text-xs text-green-600">
          LangGraph Connected
        </p>
      </div>
    </aside>
  );
}