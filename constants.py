from os.path import expanduser


HOST = "127.0.0.1"
PORT = 17171

# API is Json, WEB is HTML, RAW is raw data
TULL_API_URL = f"http://{HOST}:{PORT}/tull/api"
TULL_WEB_URL = f"http://{HOST}:{PORT}/tull/web"
TULL_RAW_URL = f"http://{HOST}:{PORT}/tull/raw"

# We make a .tull directory in case it doesn't exist TODO add configurability for this
USER_HOME = expanduser("~")
TULL_DATA_DIR = f"{USER_HOME}/.tull/data"
TULL_META_DIR = f"{USER_HOME}/.tull/meta"
