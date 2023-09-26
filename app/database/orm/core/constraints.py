from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column

id_pk = mapped_column(primary_key=True, index=True)

user_id_fk = mapped_column(ForeignKey("user.id"))
