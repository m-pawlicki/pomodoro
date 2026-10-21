import pomodoro.interval_settings as inv
from dataclasses import dataclass
from enum import Enum

class IntervalType(Enum):

    WORK = 1
    SHORT = 2
    LONG = 3

@dataclass
class Interval:

    interval_type: IntervalType
    duration: int
    position: int

def create_interval_plan(work=inv.WORK_TIME, short=inv.SHORT_TIME, long=inv.LONG_TIME, n=inv.COUNT) -> list[Interval]:

    plan_req = {"work": {"value": work, "min": inv.MIN_WORK, "max": inv.MAX_WORK}, 
            "short": {"value": short, "min": inv.MIN_SHORT, "max": inv.MAX_SHORT}, 
            "long": {"value": long, "min": inv.MIN_LONG, "max": inv.MAX_LONG}, 
            "count": {"value": n, "min": inv.MIN_COUNT, "max": inv.MAX_COUNT}
            }

    _check_plan_types(plan_req)

    _check_plan_ranges(plan_req)
        
    interval_plan: list[Interval] = []

    for i in range(1, n):
        interval_plan.append(Interval(IntervalType.WORK, work, i))
        interval_plan.append(Interval(IntervalType.SHORT, short, i))

    interval_plan.append(Interval(IntervalType.WORK, work, n))
    interval_plan.append(Interval(IntervalType.LONG, long, n))

    return interval_plan

def _check_plan_types(plan_req):

    for k, v in plan_req.items():
        if type(v["value"]) is not int:
            raise TypeError(f"{k} value {v["value"]} is not a whole number")
        

def _check_plan_ranges(plan_req):

    for k, v in plan_req.items():
        if not v["min"] <= v["value"] <= v["max"]:
            raise ValueError(f"{v["value"]} is not within {k} range of {v["min"]} - {v["max"]}")