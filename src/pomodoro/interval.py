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

        if type(work) is not int:
            raise TypeError(f"Work time {work} is not a whole number")
        
        elif type(short) is not int:
            raise TypeError(f"Short break {short} is not a whole number")
        
        elif type(long) is not int:
            raise TypeError(f"Long break {long} is not a whole number")
        
        elif type(n) is not int:
            raise TypeError(f"Interval count {n} is not a whole number")
        

        if work < inv.MIN_WORK or work > inv.MAX_WORK:
            raise ValueError(f"Work time {work} not within range {inv.MIN_WORK} - {inv.MAX_WORK}")
        
        elif short < inv.MIN_SHORT or short > inv.MAX_SHORT:
            raise ValueError(f"Short break {short} not within range {inv.MIN_SHORT} - {inv.MAX_SHORT}")
        
        elif long < inv.MIN_LONG or long > inv.MAX_LONG:
            raise ValueError(f"Long break {long} not within range {inv.MIN_LONG} - {inv.MAX_LONG}")
        
        elif n < inv.MIN_COUNT or n > inv.MAX_COUNT:
            raise ValueError(f"Interval count {n} not within range {inv.MIN_COUNT} - {inv.MAX_COUNT}")
        
  
        interval_plan: list[Interval] = []

        for i in range(1, n):
            interval_plan.append(Interval(IntervalType.WORK, work, i))
            interval_plan.append(Interval(IntervalType.SHORT, short, i))

        interval_plan.append(Interval(IntervalType.WORK, work, n))
        interval_plan.append(Interval(IntervalType.LONG, long, n))

        return interval_plan