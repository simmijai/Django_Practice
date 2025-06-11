# core/utils/logger.py
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Console Handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# Formatter
formatter = logging.Formatter('%(levelname)s | %(asctime)s | %(message)s')
ch.setFormatter(formatter)

# Add handler to logger
logger.addHandler(ch)
