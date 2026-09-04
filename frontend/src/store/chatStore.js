import { create } from "zustand";

export const useChatStore = create((set) => ({
  // Current workflow
  activeTask: "qa",
  setActiveTask: (task) => set({ activeTask: task }),

  // Selected PDFs
  selectedDocuments: [],
  toggleDocument: (doc) =>
    set((state) => ({
      selectedDocuments: state.selectedDocuments.includes(doc)
        ? state.selectedDocuments.filter((d) => d !== doc)
        : [...state.selectedDocuments, doc],
    })),

  // Current opened session
  currentSession: null,
  setCurrentSession: (id) => set({ currentSession: id }),

  // Separate chat memory for each workflow
  chats: {
    qa: [],
    literature_review: [],
    compare_papers: [],
    trend_analysis: [],
  },

  addMessage: (message) =>
    set((state) => ({
      chats: {
        ...state.chats,
        [state.activeTask]: [
          ...state.chats[state.activeTask],
          message,
        ],
      },
    })),

  replaceMessages: (messages) =>
    set((state) => ({
      chats: {
        ...state.chats,
        [state.activeTask]: messages,
      },
    })),

  clearCurrentChat: () =>
    set((state) => ({
      chats: {
        ...state.chats,
        [state.activeTask]: [],
      },
    })),
}));