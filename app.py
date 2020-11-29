import logging
from utils.config_parser import Config
from app.classifier import Classifier
from web.web_app import WebApp

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.getLevelName(Config.get_or_else("DEFAULT", "Logging", "Debug")),
                    format='%(asctime)s [%(name)s] [%(levelname)-5.5s]  %(message)s')
logger.info('Starting app')

cl = Classifier.getInstance()

if Config.getboolean_or_else("API", "ENABLED", False):
    logger.info('Starting API')
    WebApp().start()

logger.info('Done')

# hate = "Putleris durnius ar pusdurnius ar proto ligonis ar tiesiog menkystų menkysta?"
# neutral = "visi žinome, kad Kenedžiams baigėsi tragiškai tai nereikėjo rinktis tokio stiliaus.."
