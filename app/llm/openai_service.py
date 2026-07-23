from langchain_openai import ChatOpenAI

from app.core.config import settings


class OpenAIService:

    def __init__(self):

        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            api_key=settings.OPENAI_API_KEY,
            temperature=0
        )

    def generate(self, prompt: str):

        response = self.llm.invoke(prompt)

        return response.content