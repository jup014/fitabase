from fitabase.connection import Connection
import os
from dotenv import load_dotenv
from pprint import pprint

if __name__ == '__main__':
    pkey_name = "SUBSCRIPTION_PRIMARY_KEY"

    if not pkey_name in os.environ:
        load_dotenv("credentials/test.env")
    key = os.environ.get(pkey_name)

    conn = Connection(key=key)

    activity_log_list = conn.get_activity_log(start="2021-09-01", end="2021-10-14")
    pprint(len(activity_log_list))

    daily_activity_list = conn.get_daily_activity(start="2021-09-01", end="2021-10-14")
    pprint(daily_activity_list)

    sync_list = conn.get_sync_information()
    pprint(sync_list)