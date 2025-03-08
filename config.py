import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

ARXIV_API_URL = "http://export.arxiv.org/api/query"
PINECONE_API_KEY = os.getenv("pcsk_6PUmzH_58RKsC3EDHpGHL5nFX6dfNfRBZz9vQKzYKUfjrQSJcSU4m8CQxkZnjsKdqw6FEf")
PINECONE_ENVIRONMENT = "us-east1-aws"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}