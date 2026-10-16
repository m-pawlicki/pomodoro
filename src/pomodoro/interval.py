import pomodoro.interval_settings as inv
from enum import Enum

class IntervalType(Enum):
    WORK = 1
    SHORT = 2
    LONG = 3

class Interval:

    def create_interval(self, work=inv.WORK_TIME, short=inv.SHORT_TIME, long=inv.LONG_TIME, n=inv.COUNT):

        if (
            type(work) is not int
            or type(short) is not int
            or type(long) is not int
            or type(n) is not int
            ):

            raise TypeError("Interval(s) must be a whole number!")
        

        elif (
            (work < inv.MIN_WORK or work > inv.MAX_WORK)
            or (short < inv.MIN_SHORT or short > inv.MAX_SHORT)
            or (long < inv.MIN_LONG or long > inv.MAX_LONG)
            or (n < inv.MIN_COUNT or n > inv.MAX_COUNT)
            ):

            raise ValueError("Interval(s) not within range!")
        
        else:
            interval = []
            work_chunk = [IntervalType.WORK, IntervalType.SHORT]
            end_chunk = [IntervalType.WORK, IntervalType.LONG]
            for _ in range(1, n):
                interval.extend(work_chunk)
            interval.extend(end_chunk)
            return interval