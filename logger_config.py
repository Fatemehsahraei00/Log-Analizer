import logging
import os

def setup_logger():
    os.makedirs("logs", exist_ok=True)
    logger = logging.getLogger("log_analyzer")
    logger.setLevel(logging.DEBUG)

    # فرمت مشابه لاگ‌های ورودی
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s')

    # خروجی فایل
    fh = logging.FileHandler("logs/app.log")
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    # خروجی کنسول (فقط INFO و بالاتر)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger
