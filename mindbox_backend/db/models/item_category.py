from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from mindbox_backend.db import DeclarativeBase


class ItemCategory(DeclarativeBase):
    __tablename__ = "items_categories"

    id = Column(
        "id",
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    item_id = Column(
        "item_id",
        UUID(as_uuid=True),
        ForeignKey("items.id"),
        nullable=False,
    )

    category_id = Column(
        "category_id",
        UUID(as_uuid=True),
        ForeignKey("categories.id"),
        nullable=False,
    )

    category = relationship("Category", lazy="selectin")

    item = relationship("Item", lazy="selectin")
