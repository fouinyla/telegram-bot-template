from __future__ import annotations

from typing import TYPE_CHECKING, Any, Tuple, cast

import stringcase
from sqlalchemy import types
from sqlalchemy.orm import DeclarativeBase, declared_attr, registry

from .mixins import IDMixin, TimestampMixin


class ORMModel(TimestampMixin, IDMixin, DeclarativeBase):
    if TYPE_CHECKING:
        __table_args__: Tuple[Any, ...]

    registry = registry(
        type_annotation_map={
            int: types.BIGINT(),
        },
    )

    @declared_attr  # type: ignore
    def __tablename__(cls) -> str:  # noqa
        return cast(str, stringcase.snakecase(cls.__name__.split("Model")[0]))
