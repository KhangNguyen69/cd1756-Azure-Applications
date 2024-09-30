import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'khang@1234'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'udacityprj1'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'Zx6yKXpsYEeU2UDyv0XyZ7ZJ0HvrHrsgYB0XIWQoOQRK3ClEQFxGQMNES0DYhU7B/99kUZhq+JsM+AStCLcZ/A=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'udacity-project-1'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'udacity-prj-1.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'udacity_prj_1'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'khangnvt1'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Udacity@1123'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "zV18Q~zuVR0PsNE4nYipFic4S7mHDyxqQ5mfUbZM"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "72e26131-4efd-4397-be95-f5b5c5b00e61"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session