from dataclasses import dataclass
from typing import Dict, List

@dataclass(frozen=True)
class Subscription:
    name: str
    cost: float
    duration: int


@dataclass
class TravelPlan:
    """
    Rappresenta i giorni in cui si viaggia:
    True -> si viaggia
    False -> non si viaggia
    """
    days: List[bool]

    def __len__(self):
        return len(self.days)

    def is_travel_day(self, index: int) -> bool:
        return self.days[index]
    

@dataclass
class ModelConfig:
    subscriptions: List[Subscription]

    def get_cost(self) -> Dict[str, float]:
        return {s.name: s.cost for s in self.subscriptions}

    def get_durations(self) -> Dict[str, int]:
        return {s.name: s.duration for s in self.subscriptions}