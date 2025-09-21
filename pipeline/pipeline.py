from src.recommender import AnimeRecommender
from src.vector_store import VectorStoreBuilder
from config.config import GROQ_API_KEY, MODEL_NAME
from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger(__name__)

class AnimeRecommenderPipeline:
    def __init__(self, persist_directory: str="chroma_db"):
        try:
            logger.info("AnimeRecommenderPipeline initialization started.")
            self.vector_store_builder = VectorStoreBuilder(csv_path='', persist_directory=persist_directory)
            retriever = self.vector_store_builder.load_vector_store().as_retriever()
            self.recommender = AnimeRecommender(retriever, api_key=GROQ_API_KEY, model_name=MODEL_NAME)
            logger.info("AnimeRecommenderPipeline initialized successfully.")
        except Exception as e:
            logger.error(f"Error during AnimeRecommenderPipeline initialization: {e}")
            raise CustomException("Failed to initialize AnimeRecommenderPipeline", e)
    
    def recommend(self, question: str):
        try:
            logger.info("Generating recommendations.")
            recommendations = self.recommender.get_recommendations(question)
            logger.info("Recommendations generated successfully.")
            return recommendations
        except Exception as e:
            logger.error(f"Error during recommendation generation: {e}")
            raise CustomException("Failed to generate recommendations", e)