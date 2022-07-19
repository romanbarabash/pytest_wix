from environs import Env

env = Env()
env.read_env(verbose=True)

TIMEOUT = env.int('TIMEOUT', 10)
POLLING = env.float('POLLING', 0.5)

DEBUG = env.bool('DEBUG', False)

HOST = env.str('HOST')
USER_EMAIL = env.str('USER_EMAIL')
USER_PASSWORD = env.str('USER_PASSWORD')

SCREENSHOTS_DIR = '.screenshots'
CACHE_DIR = '.cache'
