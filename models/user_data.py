from dataclasses import dataclass

@dataclass
class User:
    fname: str
    lname: str
    email: str
    phone: str
    year: int
    month: str
    day: int
    subjects: str
    address: str
    sstate: str
    ccity: str