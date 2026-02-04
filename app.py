from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Any, Dict, List, Optional

app = FastAPI(title="City Name Summary")

class Record(BaseModel):
    name: Optional[str] = None
    city: Optional[str] = None
    points: Optional[int] = None

class GroupByCityRequest(BaseModel):
    records: List[Record] = Field(default_factory=list)
    normalize_city: bool = True
    sort_names: bool = True

class GroupByCityResponse(BaseModel):
    grouped: Dict[str, List[str]]

def _normalize_city(city: str) -> str:
    return city.strip().casefold()

def group_names_by_city(records: List[Record], normalize_city : bool,
    sort_names: bool) -> Dict[str, List[str]]:
    results: Dict[str, List[str]] = {}
    for Record in records:
        city = Record.city
        name = Record.name
        if name is None or city is None:
            continue
        if normalize_city:
            city = _normalize_city(city)
        if city not in results:
            results[city] = []
        results[city].append(name)
    if sort_names:
        for city in results:
            results[city].sort()
    return results

@app.post("/group-by-city", response_model=GroupByCityResponse)
def group_by_city(payload: GroupByCityRequest):
    grouped = group_names_by_city(payload.records, payload.normalize_city, payload.sort_names)
    return GroupByCityResponse(grouped=grouped)