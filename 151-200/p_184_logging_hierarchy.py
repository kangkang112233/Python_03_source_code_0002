# Explanation of Python Logging Hierarchical Structure
# TIMESTAMP__2024_08_13__133444

import logging

# Configure the parent logger
logger = logging.getLogger("parent")
logger.setLevel(logging.DEBUG)

# Create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# Create formatter and add it to the handler
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)

# Add handler to logger
logger.addHandler(ch)

# Configure the child logger
child_logger = logging.getLogger("parent.child")

# Log messages
logger.debug("This is a debug message from the parent logger.")
child_logger.info("This is an info message from the child logger.")
child_logger.error("This is an error message from the child logger.")
