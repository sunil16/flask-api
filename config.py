# -*- coding: utf-8 -*-

import os
import configparser

BRAND_NAME = "FLASK REST API"

SECRET_KEY = "df5JGZfDLMDF54RWrK_aq6Yb9HsdhdjGDDhdaPw="
UUID_LEN = 10
UUID_ALPHABET = "".join(map(chr, range(48, 58)))


APP_ENV = os.environ.get("APP_ENV") or "local"  # or 'live' to load live
INI_FILE = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "./conf/{}.ini".format(APP_ENV)
)

CONFIG = configparser.ConfigParser()
CONFIG.read(INI_FILE)

MYSQL = CONFIG["mysql"]
if APP_ENV == "dev" or APP_ENV == "live":  # credentials not available for dev and live
    DB_CONFIG = (
        MYSQL["user"],
        MYSQL["password"],
        MYSQL["host"],
        MYSQL["database"]
    )

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://%s:%s@%s/%s" % DB_CONFIG
else:
    DB_CONFIG = (MYSQL["user"], MYSQL["password"], MYSQL["host"], MYSQL["database"])
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://%s:%s@%s/%s" % DB_CONFIG

DB_ECHO = True if CONFIG["database"]["echo"] == "yes" else False
DB_AUTOCOMMIT = True

LOG_LEVEL = CONFIG["logging"]["level"]
