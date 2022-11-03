def return_predict_config():
    log_config = {
        "version": 1,
        "formatters": {
            "formatter_file": {
                "format": "%(asctime)s\t%(levelname)s\t%(message)s",
            },
            "formatter_stream": {
                "format": "%(asctime)s\t%(name)s\t%(levelname)s\t%(message)s",
            },
        },
        "handlers": {
            "file_handler": {
                "level": "DEBUG",
                "class": "logging.FileHandler",
                "filename": "src/logs/log_file_predict.log",
                "formatter": "formatter_file",
            },
            "stream_handler": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "formatter": "formatter_stream",
            },
        },
        "loggers": {
            "": {
                "level": "DEBUG",
                "handlers": ["file_handler"],
            },
            "stream_logger": {
                "level": "DEBUG",
                "handlers": ["stream_handler"],
            },
        },
    }
    return log_config

def return_train_config():
    log_config = {
        "version": 1,
        "formatters": {
            "formatter_file": {
                "format": "%(asctime)s\t%(levelname)s\t%(message)s",
            },
            "formatter_stream": {
                "format": "%(asctime)s\t%(name)s\t%(levelname)s\t%(message)s",
            },
        },
        "handlers": {
            "file_handler": {
                "level": "DEBUG",
                "class": "logging.FileHandler",
                "filename": "src/logs/log_file_train.log",
                "formatter": "formatter_file",
            },
            "stream_handler": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "formatter": "formatter_stream",
            },
        },
        "loggers": {
            "": {
                "level": "DEBUG",
                "handlers": ["file_handler"],
            },
            "stream_logger": {
                "level": "DEBUG",
                "handlers": ["stream_handler"],
            },
        },
    }
    return log_config