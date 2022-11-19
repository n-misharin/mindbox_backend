from sqlalchemy import Column, TEXT, Float, ForeignKey, Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from mindbox_backend.db import DeclarativeBase
from mindbox_backend.db.models.item_category import ItemCategory


# association_table = Table(
#     "association_table",
#     DeclarativeBase.metadata,
#     Column("item_id", ForeignKey("items.id"), primary_key=True),
#     Column("category_id", ForeignKey("categories.id"), primary_key=True),
# )


class Item(DeclarativeBase):
    __tablename__ = "items"
    id = Column(
        "id",
        UUID(as_uuid=True),
        primary_key=True,
        server_default=func.gen_random_uuid(),
    )
    title = Column(
        "title",
        TEXT,
        nullable=False,
    )
    cost = Column(
        "cost",
        Float,
        nullable=False,
    )
    categories = relationship("Category", secondary="items_categories", back_populates="items", lazy="selectin")
