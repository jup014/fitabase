from fitabase.connection import Connection
import os
from dotenv import load_dotenv
from pprint import pprint

if __name__ == '__main__':
    load_dotenv("../credentials/test.env")
    
    key = os.environ.get("SUBSCRIPTION_PRIMARY_KEY")
    
    conn = Connection(key=key)
    
    activity_log_list = conn.get_activity_log(start="2021-09-01", end="2021-10-14")
    print(len(activity_log_list))