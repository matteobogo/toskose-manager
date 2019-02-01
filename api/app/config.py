import os
import sys


class AppConfig(object):

    _LOGS_CONFIG_NAME = 'logging.conf'
    _LOGS_PATH = os.environ.get('TOSKOSE_LOGS_PATH')
    _LOGS_CONFIG_PATH = os.environ.get('TOSKOSE_LOGS_CONFIG_PATH')

    _APP_CONFIG_NAME = 'toskose.toml'
    _APP_CONFIG_PATH = os.environ.get('TOSKOSE_APP_CONFIG_PATH')
    _APP_MODE = os.environ.get('TOSKOSE_APP_MODE', default='development')


class FlaskConfig(object):
    """ Flask Base Configuration

    SECRET_KEY: used to sign cookies and other things (**important)
    DEBUG: activate the debugging mode (e.g. unhandled exceptions, reloading
    server when code changes). It is overridden by FLASK_DEBUG env.
    """

    SECRET_KEY = os.environ.get(
        'SECRET_KEY',
        default='to-iterate-is-human-to-recurse-divine')
    DEBUG = False
    TESTING = False


class DevelopmentConfig(FlaskConfig):
    """ Flask Development Configuration """

    DEBUG = True


class TestingConfig(FlaskConfig):
    """ Flask Testing Configuration """

    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = True


class ProductionConfig(FlaskConfig):
    pass

configs = dict(
    development=DevelopmentConfig,
    testing=TestingConfig,
    production=ProductionConfig
)
