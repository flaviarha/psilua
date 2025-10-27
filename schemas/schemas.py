from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import Optional, List
from models.models import UserType, AppointmentStatus, RequestStatus

#schemas 

class UserBase(BaseModel):
    email:EmailStr
    name:str
    type:UserType
    
class UserCreate(UserBase):
    password: str
    speciality: Optional[str] = None
    crp: Optional[str] = None
    phone: Optional[str] = None
    birth_date: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
class User(UserBase): 
    id: int
    speciality: Optional[str] = None
    crp: Optional[str] = None
    phone: Optional[str] = None
    created_at: datetime
    
    class Config:
         from_attributes = True  
         
class Token(BaseModel):
    acess_token: str
    token_type: str
    user: User
    
class PatientBase(BaseModel):
    name: str
    email: EmailStr
    phone: str
    birth_date: date
    
class PatientCreated(PatientBase):
    psychologis_id: int
    
class Patient(PatientBase):
    id: int
    age: int
    status: str
    psychologist_id = Optional[str] = None
    total_session: Optional[int] = 0
    created_at: datetime
    
    class Config:
        from_attributes = True
        
class AppointmentBase(BaseModel):
    patient_id= int
    psychologist_id: int
    date: date
    time: str
    description: str
    duration: Optional[int]= 50
    
class AppoitmentCreate(AppointmentBase):
    pass

class AppoitmentUpdate(AppointmentBase):
    date: Optional[date]= None
    time: Optional[str]= None
    status: Optional[AppointmentStatus]= None
    description: Optional[str]= None
    duration: Optional[int] = 50
    notes: Optional[str]= None
    full_report: Optional[str]= None
    
class RequestBase(BaseModel):
    patient_name: str
    patient_email: EmailStr
    patient_phone: str
    preferred_psychologist: int
    description: str
    urgency: str
    preferred_dates: List[str]
    preferred_time: List[str]
    
class RequestCreate(RequestBase):
    pass

class RequestUpdate(BaseModel):
    status: RequestStatus
    notes: Optional[str]= None
    
class Request(RequestBase):
    id: int
    status: RequestStatus
    notes: str
    created_at: datetime
    update_at: Optional[datetime]= None
    
    class config:
        from_attributes = True

class Psychologist(BaseModel):
    id:int
    name: str
    speciality: str
    crp: str
    
    class config:
        from_attributes = True
        
class ReportStats(BaseModel):
    active_patients: int
    total_sessions: int
    completed_session: int
    attendance_rate: int
    risk_alerts: int
    
class FrequencyData(BaseModel):
    month: str
    session: int
    
class StatusData(BaseModel):
    name: str
    value: int
    color: str
    
class RiskAlert(BaseModel):
    id: int
    patient: str
    risk: str
    reason: str
    date: str
    
class ReportsData(BaseModel):
    status: ReportStats
    frequency_data: List[FrequencyData]
    status_data: List[StatusData]
    patient_data: List[StatusData]
    risk_alerts: List[RiskAlert]