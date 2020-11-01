from datetime import datetime
from peewee import Field


class TimezoneField(Field):
    """
    A timestamp field that supports a timezone by serializing the value
    with isoformat.
    """

    field_type = "TEXT"  # This is how the field appears in Sqlite

    def db_value(self, value: datetime) -> str:
        if type(value) == str:
            obj = datetime.fromisoformat(value)
            return obj.isoformat()
        return value.isoformat()

    def python_value(self, value: str) -> str:
        if value:
            return datetime.fromisoformat(value)
