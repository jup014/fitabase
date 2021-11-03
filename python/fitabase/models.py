from datetime import datetime
from typing import List, Optional, Any
from pydantic import BaseModel, parse_obj_as

class Profile(BaseModel):
    ProfileId: Optional[str]
    CreatedDate: Optional[datetime]
    Name: Optional[str]
    
    def load_list(list_of_profile_dicts):
        m = parse_obj_as(List[Profile], list_of_profile_dicts)
        
        return m

class HeartRateZone(BaseModel):
    CaloriesOut: Optional[float]
    Max: Optional[int]
    Min: Optional[int]
    Minutes: Optional[int]
    Name: Optional[str]

class ActivityLevel(BaseModel):
    Minutes: Optional[int]
    Name: Optional[str]
    
class Activity(BaseModel):
    StartTime: Optional[datetime]
    Speed: Optional[float]
    Source: Optional[str]
    Pace: Optional[float]
    OriginalStartTime: Optional[datetime]
    OriginalDuration: Optional[int]
    CaloriesManuallySpecified: Optional[bool]
    DistanceManuallySpecified: Optional[bool]
    StepsManuallySpecified: Optional[bool]
    LogType: Optional[str]
    LogId: Optional[int]
    LastModified: Optional[datetime]
    Steps: Optional[int]
    HeartRateZones: Optional[List[HeartRateZone]]
    Duration: Optional[int]
    DistanceUnit: Optional[str]
    Distance: Optional[float]
    DateOfActivity: Optional[str]
    Calories: Optional[int]
    AverageHeartRate: Optional[int]
    ActivityTypeId: Optional[int]
    ActivityName: Optional[str]
    ActivityLevel: Optional[List[ActivityLevel]]
    ActiveDuration: Optional[int]
    ElevationGain: Optional[float]
    
    
class ActivityLog(BaseModel):
    Day: Optional[datetime]
    Activities: Optional[List[Activity]]
    
    def load_list(list_of_dicts):
        m = parse_obj_as(List[ActivityLog], list_of_dicts)
        
        return m

class DailyActivity(BaseModel):
    ActivityDate: Optional[datetime]
    TotalDistance: Optional[float]
    TrackerDistance: Optional[float]
    LoggedActivitiesDistance: Optional[float]
    VeryActiveDistance: Optional[float]
    ModeratelyActiveDistance: Optional[float]
    LightActiveDistance: Optional[float]
    SedentaryActiveDistance: Optional[float]
    VeryActiveMinutes: Optional[float]
    FairlyActiveMinutes: Optional[float]
    LightlyActiveMinutes: Optional[float]
    SedentaryMinutes: Optional[float]
    TotalSteps: Optional[int]
    Calories: Optional[int]
    Floors: Optional[int]
    CaloriesBMR: Optional[int]
    MarginalCalories: Optional[int]
    RestingHeartRate: Optional[int]
    GoalCaloriesOut: Optional[int]
    GoalDistance: Optional[float]
    GoalFloors: Optional[int]
    GoalSteps: Optional[int]
    
    def load_list(list_of_dicts):
        m = parse_obj_as(List[DailyActivity], list_of_dicts)
        
        return m

class Device(BaseModel):
    DeviceName: str
    BatteryLevel: str
    LastSync: datetime
    
    def load_list(list_of_dicts):
        m = parse_obj_as(List[Device], list_of_dicts)
        
        return m
    
class SyncInformation(BaseModel):
    SyncDate: Optional[datetime]
    LatestBatteryLevel: Optional[str]
    LatestDeviceName: Optional[str]
    SyncDateTracker: Optional[datetime]
    LatestBatteryLevelTracker: Optional[str]
    LatestDeviceNameTracker: Optional[str]
    SyncDateScale: Optional[datetime]
    LatestBatteryLevelScale: Optional[str]
    LatestDeviceNameScale: Optional[str]
    Devices: Optional[List[Device]]
    
    def load_list(list_of_dicts):
        m = parse_obj_as(List[SyncInformation], list_of_dicts)
        
        return m