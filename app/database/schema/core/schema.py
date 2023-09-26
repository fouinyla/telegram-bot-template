from __future__ import annotations

from .application_schema import ApplicationORMSchema
from .mixins import IDMixin, TimestampMixin


class ORMSchema(TimestampMixin, IDMixin, ApplicationORMSchema):
    ...
