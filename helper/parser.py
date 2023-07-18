from typing import Union


def get_data(keys: Union[list, str], data: Union[dict, list]):
    """Get payload by keys. If payload is none, return empty dict"""
    body = data
    for key in keys:
        try:
            body = body[key]
            if body is None:
                return {}
        except KeyError:
            raise KeyError(f'Data for key "{key}" is absent!')
    return body
