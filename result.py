from graph.workflow import graph

result = graph.invoke({
    "question": "What is BERT?"
})

print(result["answer"])