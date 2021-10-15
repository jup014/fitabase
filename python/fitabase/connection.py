import requests
from .models import Profile, ActivityLog

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
            'activity_log': 'https://api.fitabase.com/v1/activitylog/Get/{}/{}/{}'
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
        profile_list = Profile.load_list(response_json)
        if (len(profile_list)==1):
            self.profile_id = profile_list[0].ProfileId
        else:
            raise "Profile is not a single-item list: {}".format(profile_list)
        
        return True

    def get_activity_log(self, start:str, end:str):
        url = Constants.DICT['url']['activity_log'].format(self.profile_id, start, end)
        response_json = self.__client.get(url)
        activity_log_list = ActivityLog.load_list(response_json)
        
        return activity_log_list