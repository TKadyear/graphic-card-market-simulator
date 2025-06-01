import logging

logging.basicConfig(
    level=logging.INFO,  
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/simulation.log"),  
        logging.StreamHandler() 
    ]
)
logger = logging.getLogger(__name__)
#  Make a class o decorator which could be inside each class with dependency injection, when we only have one refference