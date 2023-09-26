from __future__ import annotations

from typing import TYPE_CHECKING, Any, Callable, Generic, List, Optional, TypeVar, Union

from pydantic import BaseConfig, BaseModel
from pydantic.generics import GenericModel
from pydantic.utils import GetterDict
from sqlalchemy import inspect
from sqlalchemy.orm.attributes import instance_state

if TYPE_CHECKING:
    from pydantic.typing import (
        AbstractSetIntStr,
        DictStrAny as PydanticDictStrAny,
        MappingIntStrAny,
    )

from typing import Any, Dict


DictStrAny = Dict[str, Any]


class ExcludeNone:
    def dict(
        self,
        *,
        include: Optional[Union[AbstractSetIntStr, MappingIntStrAny]] = None,
        exclude: Optional[Union[AbstractSetIntStr, MappingIntStrAny]] = None,
        by_alias: bool = False,
        skip_defaults: Optional[bool] = None,
        exclude_unset: bool = False,
        exclude_defaults: bool = False,
        exclude_none: bool = False,
    ) -> PydanticDictStrAny:
        exclude_none = True

        return super(ExcludeNone, self).dict(  # type: ignore
            include=include,
            exclude=exclude,
            by_alias=by_alias,
            skip_defaults=skip_defaults,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
        )

    def json(
        self,
        *,
        include: Optional[Union[AbstractSetIntStr, MappingIntStrAny]] = None,
        exclude: Optional[Union[AbstractSetIntStr, MappingIntStrAny]] = None,
        by_alias: bool = False,
        skip_defaults: Optional[bool] = None,
        exclude_unset: bool = False,
        exclude_defaults: bool = False,
        exclude_none: bool = False,
        encoder: Optional[Callable[[Any], Any]] = None,
        models_as_dict: bool = True,
        **dumps_kwargs: Any,
    ) -> str:
        exclude_none = True

        return super(ExcludeNone, self).json(  # type: ignore
            include=include,
            exclude=exclude,
            by_alias=by_alias,
            skip_defaults=skip_defaults,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
            encoder=encoder,
            models_as_dict=models_as_dict,
            **dumps_kwargs,
        )


class ApplicationSchema(ExcludeNone, BaseModel):
    class Config(BaseConfig):
        allow_population_by_field_name = True
        smart_union = True
        min_anystr_length = 1


class IgnoreLazyGetterDict(GetterDict):
    def __init__(self, obj: Any):
        super(IgnoreLazyGetterDict, self).__init__(obj=obj)
        self._keys = [r.key for r in inspect(self._obj.__class__).relationships]

    def __getitem__(self, key: str) -> Any:
        if self._is_lazy_loaded(key):
            return None

        return getattr(self._obj, key)

    def get(self, key: Any, default: Any = None) -> Any:
        if self._is_relationship(key) and self._is_lazy_loaded(key):
            return None

        return getattr(self._obj, key, default)

    def _is_lazy_loaded(self, key: Any) -> bool:
        return key in instance_state(self._obj).unloaded

    def _is_relationship(self, key: Any) -> bool:
        return key in self._keys


class ApplicationORMSchema(ApplicationSchema):
    class Config(BaseConfig):
        orm_mode = True
        getter_dict = IgnoreLazyGetterDict


DetailT = Union[
    str,
    List[str],
    List[DictStrAny],
    DictStrAny,
]
ErrorT = Union[
    str,
    List[str],
    List[DictStrAny],
    DictStrAny,
]
ResponseT = TypeVar("ResponseT", bound=Any)


class ApplicationResponse(ExcludeNone, GenericModel, Generic[ResponseT]):
    class Config:
        allow_population_by_field_name = True
        smart_union = True
        orm_mode = True

    ok: bool
    result: Optional[ResponseT] = None
    detail: Optional[DetailT] = None
    error: Optional[ErrorT] = None
    error_code: Optional[int] = None
