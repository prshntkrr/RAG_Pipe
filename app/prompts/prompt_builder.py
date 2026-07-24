class PromptBuilder:

    @staticmethod
    def build(question: str, search_result: dict):

        documents = search_result["documents"][0]

        context = "\n\n".join(documents)

        return f"""
            You are an agricultural expert.

            Answer ONLY from the provided context.

            If the answer is not present in the context, reply:

            'I couldn't find this information in the uploaded documents.'

            Context:
            {context}

            Question:
            {question}

            Answer:
            """