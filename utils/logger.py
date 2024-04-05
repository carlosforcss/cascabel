import logging

logger_instance = None


def get_logger():
    # Create logger
    global logger_instance
    if logger_instance:
        return logger_instance
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler("logs.txt")
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger_instance = logger
    return logger_instance
