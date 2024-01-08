# Get the database using the method we defined in pymongo_test_insert file
from admin_app.db_config import get_database
dbname = get_database()

def get_collection():
    return dbname["indeed_jobs"]