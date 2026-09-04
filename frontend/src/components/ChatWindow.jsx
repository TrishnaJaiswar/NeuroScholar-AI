import { useState } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import api from "../services/api";
import { useChatStore } from "../store/chatStore";

export default function ChatWindow() {
  const [input, setInput] = useState("");

  const {
    addMessage,
    activeTask,
    selectedDocuments,
  } = useChatStore();

  const messages = useChatStore(
    (state) => state.chats[state.activeTask]
  );

  const handleSend = async () => {
    if (!input.trim()) return;

    addMessage({
      role: "user",
      content: input,
    });

    const question = input;
    setInput("");

    try {
      const res = await api.post("/chat", {
        question,
        task: activeTask,
        documents: selectedDocuments,
      });

      addMessage({
        role: "assistant",
        content: res.data.answer,
        citations: res.data.citations || [],
      });
    } catch (error) {
      addMessage({
        role: "assistant",
        content: "Unable to connect to NeuroScholar AI backend.",
      });

      console.error(error);
    }
  };

  const getTaskLabel = () => {
    switch (activeTask) {
      case "literature_review":
        return "Literature Review";
      case "compare_papers":
        return "Compare Papers";
      case "trend_analysis":
        return "Trend Analysis";
      default:
        return "Research Chat";
    }
  };

  const getPlaceholder = () => {
    switch (activeTask) {
      case "literature_review":
        return "Generate a literature review from selected PDFs...";
      case "compare_papers":
        return "Compare the selected research papers...";
      case "trend_analysis":
        return "Analyze trends across selected papers...";
      default:
        return "Ask anything about selected research papers...";
    }
  };

  return (
    <main className="flex-1 bg-gray-50 flex flex-col">
      {/* Header */}
      <div className="px-6 pt-5 flex items-center justify-between">
        <span className="inline-flex items-center rounded-full bg-blue-100 px-3 py-1 text-sm font-medium text-blue-700">
          {getTaskLabel()}
        </span>

        {selectedDocuments.length > 0 && (
          <span className="text-xs text-gray-500">
            {selectedDocuments.length} PDF selected
          </span>
        )}
      </div>

      {/* Chat */}
      <div className="flex-1 overflow-y-auto p-6 space-y-6">
        {messages.length === 0 && (
          <div className="text-center mt-20">
            <h2 className="text-3xl font-bold text-gray-800">
              Welcome to NeuroScholar AI
            </h2>

            <p className="text-gray-500 mt-3">
              {getPlaceholder()}
            </p>
          </div>
        )}

        {messages.map((msg, index) =>
          msg.role === "user" ? (
            <div key={index} className="flex justify-end">
              <div className="bg-blue-600 text-white rounded-2xl px-4 py-3 max-w-xl">
                {msg.content}
              </div>
            </div>
          ) : (
            <div key={index} className="flex gap-3">
              <div className="w-10 h-10 rounded-full bg-blue-600 text-white flex items-center justify-center font-bold shrink-0">
                AI
              </div>

              <div className="bg-white border border-gray-200 rounded-2xl p-5 max-w-3xl shadow-sm">
                <article className="prose prose-gray max-w-none">
                  <ReactMarkdown remarkPlugins={[remarkGfm]}>
                    {msg.content}
                  </ReactMarkdown>
                </article>

                {msg.citations?.length > 0 && (
                  <div className="mt-5 border-t pt-4">
                    <h4 className="font-semibold text-sm text-gray-700 mb-3">
                      Sources
                    </h4>

                    <div className="space-y-3">
                      {msg.citations.map((cite, i) => (
                        <div
                          key={i}
                          className="rounded-lg border bg-gray-50 p-3"
                        >
                          <div className="flex justify-between mb-2">
                            <span className="text-sm font-semibold text-blue-700">
                              {cite.source}
                            </span>

                            <span className="text-xs text-gray-500">
                              Page {cite.page}
                            </span>
                          </div>

                          <p className="text-sm italic text-gray-700">
                            "{cite.quote}"
                          </p>
                        </div>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            </div>
          )
        )}
      </div>

      {/* Input */}
      <div className="border-t bg-white p-4">
        <div className="border rounded-xl px-4 py-3 flex gap-3">
          <input
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && handleSend()}
            className="flex-1 outline-none"
            placeholder={getPlaceholder()}
          />

          <button
            onClick={handleSend}
            className="bg-blue-600 hover:bg-blue-700 text-white px-5 rounded-lg"
          >
            Send
          </button>
        </div>
      </div>
    </main>
  );
}