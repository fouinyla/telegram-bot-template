from __future__ import annotations

from datetime import datetime

import pytz
from sqlalchemy import text as t
from sqlalchemy import types, func
from sqlalchemy.orm import mapped_column
from typing_extensions import Annotated

from . import constraints

bool_no_value = Annotated[bool, mapped_column(types.Boolean)]
bool_false = Annotated[bool, mapped_column(types.Boolean, default=False, nullable=True)]
bool_true = Annotated[bool, mapped_column(types.Boolean, default=True, nullable=True)]

created_at_timezone = Annotated[
    datetime, mapped_column(types.DateTime(timezone=True), server_default=func.now())
]
updated_at_timezone = Annotated[
    datetime,
    mapped_column(
        types.DateTime(timezone=True),
        server_default=func.now(),
        server_onupdate=func.now(),
    ),
]
datetime_timezone = Annotated[datetime, mapped_column(types.DateTime(timezone=True))]
moscow_datetime_timezone = Annotated[
    datetime,
    mapped_column(
        default=datetime.now(tz=pytz.timezone("Europe/Moscow")),
        type_=types.TIMESTAMP(timezone=True),
    ),
]

decimal_10_2 = Annotated[float, mapped_column(types.DECIMAL(10, 2))]
decimal_3_2 = Annotated[float, mapped_column(types.DECIMAL(3, 2))]
decimal_2_1 = Annotated[float, mapped_column(types.DECIMAL(2, 1))]

small_int = Annotated[
    int, mapped_column(types.SMALLINT, nullable=False, server_default=t("1"))
]
big_int = Annotated[int, mapped_column(types.BIGINT)]
int = Annotated[int, mapped_column(types.INTEGER)]

str_200 = Annotated[str, mapped_column(types.String(200))]  # for email use
str_100 = Annotated[str, mapped_column(types.String(100))]
str_50 = Annotated[str, mapped_column(types.String(50))]
str_36 = Annotated[str, mapped_column(types.String(36))]
str_30 = Annotated[str, mapped_column(types.String(30))]
str_25 = Annotated[str, mapped_column(types.String(25))]
str_20 = Annotated[str, mapped_column(types.String(20))]
str_16 = Annotated[str, mapped_column(types.String(16))]
str_15 = Annotated[str, mapped_column(types.String(15))]
str_14 = Annotated[str, mapped_column(types.String(14))]
str_4 = Annotated[str, mapped_column(types.String(4))]
text = Annotated[str, mapped_column(types.Text)]

id_pk_type = Annotated[int, constraints.id_pk]
