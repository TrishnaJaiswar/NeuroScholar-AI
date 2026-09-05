import { create } from "zustand";

export const useChatStore = create((set) => ({

  // ---------------- Current workflow ----------------

  activeTask: "qa",

  setActiveTask: (task) =>
    set({
      activeTask: task,
    }),

  // ---------------- Selected PDFs ----------------

  selectedDocuments: [],

  toggleDocument: (doc) =>
    set((state) => ({
      selectedDocuments: state.selectedDocuments.includes(doc)
        ? state.selectedDocuments.filter((d) => d !== doc)
        : [...state.selectedDocuments, doc],
    })),

  setSelectedDocuments: (documents) =>
    set({
      selectedDocuments: documents,
    }),

  // ---------------- Current opened session ----------------

  currentSession: null,

  setCurrentSession: (id) =>
    set({
      currentSession: id,
    }),

  // ---------------- Chat memory ----------------

  chats: {
    qa: [],
    literature_review: [],
    compare_papers: [],
    trend_analysis: [],
  },

  // ---------------- Add message ----------------

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

  // ---------------- Replace messages ----------------

  replaceMessages: (messages) =>
    set((state) => ({
      chats: {
        ...state.chats,

        [state.activeTask]: messages,
      },
    })),

  // ---------------- Update last assistant message ----------------
  // Used for token-by-token streaming

  updateLastAssistantMessage: (content) =>
    set((state) => {
      const currentChat =
        state.chats[state.activeTask];

      if (!currentChat || currentChat.length === 0) {
        return state;
      }

      const updatedChat = [...currentChat];

      const lastIndex =
        updatedChat.length - 1;

      updatedChat[lastIndex] = {
        ...updatedChat[lastIndex],
        content,
      };

      return {
        chats: {
          ...state.chats,

          [state.activeTask]: updatedChat,
        },
      };
    }),

  // ---------------- Clear current chat ----------------

  clearCurrentChat: () =>
    set((state) => ({
      chats: {
        ...state.chats,

        [state.activeTask]: [],
      },
    })),

}));