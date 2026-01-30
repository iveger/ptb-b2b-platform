import time
from loguru import logger

START_TIME = time.time()


def on_startup():
    logger.info("🚀 Application startup")


def on_shutdown():
    uptime = int(time.time() - START_TIME)
    logger.info(f"🛑 Application shutdown. Uptime: {uptime}s")
