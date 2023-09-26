from __future__ import annotations

from pydantic import BaseModel


class IDMixin(BaseModel):
    id: int
