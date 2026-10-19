import pomodoro.interval_settings as inv
from dataclasses import dataclass
from enum import Enum

class IntervalType(Enum):
    WORK = 1
    SHORT = 2
    LONG = 3

@dataclass
class Interval:
    name: IntervalType
    duration: int
    position: int

def create_interval_plan(work=inv.WORK_TIME, short=inv.SHORT_TIME, long=inv.LONG_TIME, n=inv.COUNT) -> list[Interval]:

        if (
            type(work) is not int
            or type(short) is not int
            or type(long) is not int
            or type(n) is not int
            ):

            raise TypeError("Interval must use whole numbers")
        

        elif (
            (work < inv.MIN_WORK or work > inv.MAX_WORK)
            or (short < inv.MIN_SHORT or short > inv.MAX_SHORT)
            or (long < inv.MIN_LONG or long > inv.MAX_LONG)
            or (n < inv.MIN_COUNT or n > inv.MAX_COUNT)
            ):

            raise ValueError("Interval not within range")
        
        else:
            interval_plan: list[Interval] = []
            for i in range(1, n):
                interval_plan.append(Interval(IntervalType.WORK, work, i))
                interval_plan.append(Interval(IntervalType.SHORT, short, i))
            interval_plan.append(Interval(IntervalType.WORK, work, n))
            interval_plan.append(Interval(IntervalType.LONG, long, n))
            return interval_plan