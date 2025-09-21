from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
from src.prompt_template import get_anime_prompt

class AnimeRecommender:
    def __init__(self, retriever,api_key: str, model_name: str):
        self.retriever = retriever
        self.api_key = api_key
        self.model_name = model_name
        self.llm = ChatGroq(api_key=self.api_key, model_name=self.model_name,temperature=0)
        self.prompt = get_anime_prompt()
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.retriever,
            return_source_documents=True,
            chain_type_kwargs={"prompt": self.prompt}
        )
    
    def get_recommendations(self, question: str):
        response = self.qa_chain.invoke(question)
        return response['result']
    