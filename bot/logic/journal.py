from sqlalchemy import Table, Column, Integer, String, DateTime, MetaData
import datetime

metadata = MetaData()

journal_entries = Table(
    "journal_entries",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("text", String, nullable=False),
    Column("emotion", String),
    Column("timestamp", DateTime, default=datetime.datetime.utcnow),
)
