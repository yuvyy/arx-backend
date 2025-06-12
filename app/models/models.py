from sqlmodel import Field, Relationship, SQLModel
from typing import Optional, List
from datetime import datetime, timezone

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(index=True, unique=True, nullable=False)
    hashed_password: str = Field(nullable=False)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))  # Corrected here
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))  # Corrected here
    password: List["Password"] = Relationship(back_populates="owner")


class Password(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    service_name: str = Field(index=True, nullable=False)
    password_hash: str = Field(nullable=False)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))  # Corrected here
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))  # Corrected here
    user_id: int = Field(foreign_key="user.id", nullable=False)
    owner: User = Relationship(back_populates="password")

class BlackListToken(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    token: str = Field(index=True, nullable=False)
    invalidated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))  # Corrected here
