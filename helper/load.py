from importlib import import_module


def load_json_schema(path: str, json_schema: str = 'schema'):
    """Json-schema loaded from file"""
    module = import_module(f'schema.{path}')
    return getattr(module, json_schema)


def load_data(path: str, test_data: str = 'data'):
    """Load test data from file for tests parametrize"""
    module = import_module(f'data.{path}')
    return getattr(module, test_data)
