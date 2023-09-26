from __future__ import annotations

from typing import Optional

from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped

from ..types import str_50


class NameMixin:
    first_name: Mapped[Optional[str_50]]
    last_name: Mapped[Optional[str_50]]

    @hybrid_property
    def full_name(self) -> Optional[str]:
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        if self.first_name:
            return f"{self.first_name}"
        if self.last_name:
            return f"{self.last_name}"
        return None
