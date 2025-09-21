import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.data_loader import animeDataLoader
from src.vector_store import VectorStoreBuilder
from src.recommender import AnimeRecommender
from utils.logger import get_logger
from utils.custom_exception import CustomException
from dotenv import load_dotenv
load_dotenv()
logger = get_logger("build_pipeline")
def main():
    try:
        logger.info("Starting the Anime Recommender Pipeline")
        
        # Step 1: Load and preprocess data
        data_loader = animeDataLoader(original_path='data/anime_with_synopsis.csv', processed_path='data/processed_anime.csv')
        processed_csv = data_loader.load_process()

        logger.info("Data loaded and preprocessed successfully")
        # Step 2: Build and save vector store
        vector_store_builder = VectorStoreBuilder(csv_path='data/processed_anime.csv', persist_directory='chroma_db')
        
        vector_store_builder.build_save_vector_store()
        logger.info("Vector store built and saved successfully")
    except Exception as e:
        logger.error(f"Error in main pipeline: {e}")
        raise CustomException("Error occurred in the main pipeline", e)

if __name__ == "__main__":
    main()
