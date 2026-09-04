const reviews = [
  {
    name: "Research Student",
    role: "M.Tech AI",
    review:
      "NeuroScholar reduced my literature review time from days to hours. The citation verification is incredibly useful.",
  },
  {
    name: "PhD Scholar",
    role: "Computer Science",
    review:
      "The paper comparison feature makes it easy to analyze methodologies and experimental results across multiple papers.",
  },
  {
    name: "ML Engineer",
    role: "GenAI Research",
    review:
      "Advanced RAG with LangGraph gives much more reliable answers than a normal chatbot.",
  },
];

export default function Testimonials() {
  return (
    <section className="bg-white py-24">
      <div className="max-w-7xl mx-auto px-6">
        <div className="text-center mb-16">
          <span className="bg-blue-100 text-blue-700 px-4 py-2 rounded-full text-sm font-medium">
            Testimonials
          </span>

          <h2 className="text-5xl font-bold mt-6">
            Loved by Researchers
          </h2>

          <p className="text-gray-600 mt-5">
            Designed for students, researchers and AI engineers.
          </p>
        </div>

        <div className="grid md:grid-cols-3 gap-8">
          {reviews.map((r, i) => (
            <div
              key={i}
              className="border border-gray-200 rounded-3xl p-8 hover:shadow-lg transition"
            >
              <div className="flex text-yellow-400 text-xl mb-4">
                ★★★★★
              </div>

              <p className="text-gray-600 leading-7">
                "{r.review}"
              </p>

              <div className="mt-6">
                <h4 className="font-bold">{r.name}</h4>
                <p className="text-sm text-gray-500">{r.role}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}