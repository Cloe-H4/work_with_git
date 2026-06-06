# import os
# import logging
# from sqlalchemy import create_engine, text
# from dotenv import load_dotenv
import gc

gc.collect()

# # Setup logging
# os.makedirs("logs", exist_ok=True)
# logging.basicConfig(
#     filename=os.path.join("logs", "warehouse.log"),
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s",
#     filemode="a"
# )
# logging.info("========== WAREHOUSE PIPELINE STARTED ==========")

# # Load database credentials
# load_dotenv()
# DB_NAME = os.getenv("DB_NAME")
# DB_USER = os.getenv("DB_USER")
# DB_PASSWORD = os.getenv("DB_PASSWORD")
# DB_HOST = os.getenv("DB_HOST")
# DB_PORT = os.getenv("DB_PORT")
# engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
# logging.info("Database engine created successfully")

# # Function to execute SQL files
# def run_sql_file(filepath):
#     logging.info(f"Running {filepath}")
#     with open(filepath, 'r') as file:
#         sql = file.read()
#     with engine.begin() as conn:
#         conn.execute(text(sql))
#     logging.info(f"Completed {filepath}")

# # List of SQL files in order
# sql_files = [
#     "sql/drop_tables.sql",
#     "sql/dim_movies.sql",
#     "sql/dim_genres.sql",
#     "sql/bridge_movie_genres.sql",
#     "sql/fact_ratings.sql",
#     "sql/indexes.sql"
# ]

# # Execute all
# try:
#     for f in sql_files:
#         run_sql_file(f)
# except Exception as e:
#     logging.error(f"Warehouse build failed: {e}")
#     raise

# logging.info("========== WAREHOUSE PIPELINE COMPLETED ==========")
