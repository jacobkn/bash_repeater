import logging


def get_logger(log_level: str = "INFO"):
    return logging.basicConfig(format='%(asctime)s.%(msecs)03d %(levelname)s {%(module)s} [%(funcName)s] %(message)s',
                        datefmt='%Y-%m-%d,%H:%M:%S',
                        level=log_level)