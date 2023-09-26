from __future__ import annotations

from sqlalchemy.orm import Mapped

from ..constraints import id_pk
from ..types import id_pk_type


class IDMixin:
    id: Mapped[id_pk_type] = id_pk
