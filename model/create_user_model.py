from dataclasses import dataclass, asdict


@dataclass
class RequestCreateUserModel:
    """Class for Request params"""
    name: str
    job: str

    def to_dict(self):
        """Converting to dict to send body"""
        return asdict(self)


@dataclass
class ResponseCreateUserModel:
    """Class for Response params"""
    name: str
    job: str
    last_name: str
    id_: str
    created_at: str
