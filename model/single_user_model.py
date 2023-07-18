from dataclasses import dataclass


@dataclass
class ResponseSingleUserModel:
    """Class for Response params"""
    id_: int
    email: str
    first_name: str
    last_name: str
    avatar: str
    url: str
    text: str
