"""
DB queries.
"""

from sqlalchemy.ext.asyncio import AsyncConnection
from sqlalchemy.sql import select

from .db import metadata


async def fetch_flags(conn: AsyncConnection):
    flags = metadata.tables['flags']
    records = await conn.execute(select(flags))
    return records


async def fetch_flag(conn: AsyncConnection, id: int):
    flags = metadata.tables['flags']

    stmt = select(flags).where(flags.c.user_id == id)
    records = await conn.execute(stmt)
    return records
