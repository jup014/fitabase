import requests
from .models import Profile, ActivityLog, DailyActivity, SyncInformation

class HttpClient:
    def __init__(self):
        self.headers = {}
    
    def set_header(self, key, value):
        self.headers[key] = value
        
    def get(self, url, params=None):
        response = requests.get(url, params=params, headers=self.headers)
        
        return response.json()

class Constants:
    DICT = {
        'url': {
            'profile': 'https://api.fitabase.com/v1/Profiles/',
            'activity_log': 'https://api.fitabase.com/v1/activitylog/Get/{}/{}/{}',
            'daily_activity': 'https://api.fitabase.com/v1/DailyActivity/{}/{}/{}',
            'sync_information': 'https://api.fitabase.com/v1/Sync/Latest/{}'
        }
    }
    
class Connection:
    def __init__(self, key):
        self.__key = key
        self.__client = HttpClient()
        self.__client.set_header('Ocp-Apim-Subscription-Key', self.__key)
        self.__authenticate()
    
    def __authenticate(self):
        response_json = self.__client.get(Constants.DICT['url']['profile'])
        self.profiles = Profile.load_list(response_json)
        return True

    def get_activity_log(self, start:str, end:str, profile:Profile=None):
        if profile is None:
            return [{"profile": x, "activity_logs": self.get_activity_log(start, end, x)} for x in self.profiles]
        
        url = Constants.DICT['url']['activity_log'].format(profile.ProfileId, start, end)
        response_json = self.__client.get(url)
        activity_log_list = ActivityLog.load_list(response_json)
        
        return activity_log_list

    def get_daily_activity(self, start:str, end:str, profile:Profile=None):
        if profile is None:
            return [{"profile": x, "daily_activity": self.get_daily_activity(start, end, x)} for x in self.profiles]
        
        url = Constants.DICT['url']['daily_activity'].format(profile.ProfileId, start, end)
        response_json = self.__client.get(url)
        activity_log_list = DailyActivity.load_list(response_json)
        
        return activity_log_list
    
    def get_sync_information(self, profile:Profile=None):
        if profile is None:
            return [{"profile": x, "daily_activity": self.get_sync_information(x)} for x in self.profiles]
        
        url = Constants.DICT['url']['sync_information'].format(profile.ProfileId)
        response_json = self.__client.get(url)
        sync_information = SyncInformation().parse_obj(response_json)
        
        return sync_information