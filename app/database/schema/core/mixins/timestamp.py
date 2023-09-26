from __future__ import annotations

import datetime as dt
from typing import Optional

from pydantic import BaseModel


class TimestampMixin(BaseModel):
    created_at: Optional[dt.datetime]
    updated_at: Optional[dt.datetime]
