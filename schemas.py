from pydantic import BaseModel
from typing import Optional

class Ticket(BaseModel):
    userid: int
    issue_description: str
    categoryid: Optional[int] = 0

class CreateTicket(Ticket):
    pass

class Get(BaseModel):
    userid = int
    ticketid = int

class CreateUser(BaseModel):
    username: str
    password: str
    email: str = ""

class CreateMessage(BaseModel):
    userid: int
    ticketid: int
    message: str

class CreateProgress(BaseModel):
    ticketid: int
    statusid: int
    technicianid: int
    message: Optional[str] = None

