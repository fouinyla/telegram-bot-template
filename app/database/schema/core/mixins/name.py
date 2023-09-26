from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class NameMixin(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    full_name: Optional[str] = None
