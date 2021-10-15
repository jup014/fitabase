from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, parse_obj_as

class Profile(BaseModel):
    ProfileId: str
    CreatedDate: datetime
    Name: str
    
    def load_list(list_of_profile_dicts):
        m = parse_obj_as(List[Profile], list_of_profile_dicts)
        
        return m

class HeartRateZone(BaseModel):
    CaloriesOut: float
    Max: int
    Min: int
    Minutes: int
    Name: str

class ActivityLevel(BaseModel):
    Minutes: int
    Name: str
    
class Activity(BaseModel):
    StartTime: datetime
    Speed: float
    Source: Optional[str]
    Pace: float
    OriginalStartTime: datetime
    OriginalDuration: int
    CaloriesManuallySpecified: bool
    DistanceManuallySpecified: bool
    StepsManuallySpecified: bool
    LogType: str
    LogId: int
    LastModified: datetime
    Steps: int
    HeartRateZones: List[HeartRateZone]
    Duration: int
    DistanceUnit: Optional[str]
    Distance: float
    DateOfActivity: str
    Calories: int
    AverageHeartRate: int
    ActivityTypeId: int
    ActivityName: str
    ActivityLevel: List[ActivityLevel]
    ActiveDuration: int
    ElevationGain: float
    
    
class ActivityLog(BaseModel):
    Day: datetime
    Activities: List[Activity]
    
    def load_list(list_of_dicts):
        m = parse_obj_as(List[ActivityLog], list_of_dicts)
        
        return m