# Logging Levels in Python
# TIMESTAMP__2024_08_03__143417
# This example demonstrates the use of different logging levels in a library management system.

import logging

# Configure logging
logging.basicConfig(level=logging.ERROR)

logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
