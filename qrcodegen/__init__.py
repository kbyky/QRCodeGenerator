import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s  -  %(module)s.%(funcName)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logging.getLogger(__name__).addHandler(logging.NullHandler())

logger = logging.getLogger(__name__)
