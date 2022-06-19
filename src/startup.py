import configurations.configure as cfg


def startup():
    """
    Configure the application.
    """
    cfg.add_env()
    cfg.add_logging()
    cfg.add_telegram_bot()