import { Link } from "react-router-dom";
import { ArrowRight } from "lucide-react";

export default function CTA() {
  return (
    <section className="bg-blue-600 py-24">
      <div className="max-w-5xl mx-auto px-6 text-center text-white">

        <h2 className="text-5xl font-bold leading-tight">
          Ready to Transform Your Research Workflow?
        </h2>

        <p className="text-blue-100 text-lg mt-6 leading-8">
          Upload PDFs, ask technical questions, generate literature reviews,
          compare papers and obtain citation-backed answers—all in one platform.
        </p>

        <Link
          to="/dashboard"
          className="inline-flex items-center gap-2 mt-10 bg-white text-blue-600 px-8 py-4 rounded-xl font-semibold hover:bg-gray-100 transition"
        >
          Launch NeuroScholar AI
          <ArrowRight size={20} />
        </Link>

      </div>
    </section>
  );
}