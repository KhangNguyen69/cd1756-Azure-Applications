import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'khang@1234'  # Use environment variable in production

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'udacityprj1'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'Zx6yKXpsYEeU2UDyv0XyZ7ZJ0HvrHrsgYB0XIWQoOQRK3ClEQFxGQMNES0DYhU7B/99kUZhq+JsM+AStCLcZ/A=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'udacity-project-1'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'udacity-prj-1.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'udacity_prj_1'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'khangnvt1'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Udacity@1123'

    # Corrected SQLAlchemy connection string
    SQLALCHEMY_DATABASE_URI = (
        'mssql+pyodbc://{username}:{password}@{server}:1433/{database}?driver=ODBC+Driver+17+for+SQL+Server'
    ).format(
        username=SQL_USER_NAME,
        password=SQL_PASSWORD,
        server=SQL_SERVER,
        database=SQL_DATABASE
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    CLIENT_SECRET = os.getenv("CLIENT_SECRET") or "zV18Q~zuVR0PsNE4nYipFic4S7mHDyxqQ5mfUbZM"  # Replace with env var for production

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    CLIENT_ID = "72e26131-4efd-4397-be95-f5b5c5b00e61"

    REDIRECT_PATH = "/getAToken"  # Ensure this matches your app's redirect_uri in AAD

    SCOPE = ["User.Read"]  # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
