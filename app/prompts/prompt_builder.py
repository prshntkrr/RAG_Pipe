class PromptBuilder:

    @staticmethod
    def build(
        question: str,
        search_result: dict
    ):

        documents = search_result["documents"][0]

        context = "\n\n".join(documents)

        prompt = f"""
You are a helpful AI assistant.

Answer ONLY using the following context.

Context:

{context}

Question:

{question}

Answer:
"""

        return prompt