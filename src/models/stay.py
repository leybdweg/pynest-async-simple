from __future__ import annotations

from typing import Dict, Any

from pydantic import BaseModel


class ProviderData(BaseModel):
    quote: Any


class Stay(BaseModel):
    request_id: str | None
    ski_site: int
    from_date: str
    to_date: str
    group_size: int
    provider_datas = {}  #: Dict[str, ProviderData] = {}
