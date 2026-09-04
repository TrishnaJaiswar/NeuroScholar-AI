import Sidebar from "../components/Sidebar";
import Topbar from "../components/Topbar";
import ChatWindow from "../components/ChatWindow";
import Workspace from "../components/Workspace";

export default function DashboardLayout() {
  return (
    <div className="h-screen w-full bg-white flex overflow-hidden">
      <Sidebar />

      <div className="flex-1 flex flex-col">
        <Topbar />

        <div className="flex flex-1 overflow-hidden">
          <ChatWindow />
          <Workspace />
        </div>
      </div>
    </div>
  );
}