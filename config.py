from environs import Env

env = Env()
env.read_env(verbose=True)

TIMEOUT = env.int('TIMEOUT', 30)
POLLING = env.float('POLLING', 0.5)

COMPARE_TEXT = env.bool('COMPARE_TEXT', True)
DEBUG = env.bool('DEBUG', False)

HOST = env.str('HOST')
USER_EMAIL = env.str('USER_EMAIL')
USER_PASSWORD = env.str('USER_PASSWORD')

SCREENSHOTS_DIR = '.screenshots'
DOWNLOADS_DIR = '.downloads'
CACHE_DIR = '.cache'
