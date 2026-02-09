import logging
from config import ENV

level = logging.DEBUG if ENV == "dev" else logging.INFO

logging.basicConfig(
    level=level,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)