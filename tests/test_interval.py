import pomodoro.interval as pomo
import pytest
from contextlib import nullcontext

class TestInterval:

    def test_default_vals(self):
        res = pomo.create_interval_plan()
        assert res == [
            pomo.Interval(pomo.IntervalType.WORK, 25,1),
            pomo.Interval(pomo.IntervalType.SHORT, 5,1),
            pomo.Interval(pomo.IntervalType.WORK, 25,2),
            pomo.Interval(pomo.IntervalType.SHORT, 5,2),
            pomo.Interval(pomo.IntervalType.WORK, 25,3),
            pomo.Interval(pomo.IntervalType.SHORT, 5,3),
            pomo.Interval(pomo.IntervalType.WORK, 25,4),
            pomo.Interval(pomo.IntervalType.LONG, 20,4),
            ]

    def test_default_length(self):
        res = pomo.create_interval_plan()
        assert len(res) == 8


    # Within range, outside upper + lower ranges, at min + max, float, bool

    testdata_work = [(42, nullcontext(42)),
                     (pomo.inv.MIN_WORK-1, pytest.raises(ValueError, match="work")),
                     (pomo.inv.MAX_WORK+1, pytest.raises(ValueError, match="work")),
                     (pomo.inv.MIN_WORK, nullcontext(pomo.inv.MIN_WORK)),
                     (pomo.inv.MAX_WORK,  nullcontext(pomo.inv.MAX_WORK)),
                     (60.9, pytest.raises(TypeError, match="work")),
                     (True, pytest.raises(TypeError, match="work"))]
    
    @pytest.mark.parametrize("work,expected", testdata_work)
    def test_work_param(self, work, expected):
        with expected as e:
            res = pomo.create_interval_plan(work = work)
            assert res[-2].duration == e
           


    testdata_short = [(12, nullcontext(12)),
                     (pomo.inv.MIN_SHORT-1, pytest.raises(ValueError, match="short")),
                     (pomo.inv.MAX_SHORT+1, pytest.raises(ValueError, match="short")),
                     (pomo.inv.MIN_SHORT, nullcontext(pomo.inv.MIN_SHORT)),
                     (pomo.inv.MAX_SHORT,  nullcontext(pomo.inv.MAX_SHORT)),
                     (10.5, pytest.raises(TypeError, match="short")),
                     (True, pytest.raises(TypeError, match="short"))]
    
    @pytest.mark.parametrize("short,expected", testdata_short)
    def test_short_param(self, short, expected):
        with expected as e:
            res = pomo.create_interval_plan(short = short)
            assert res[-3].duration == e
    

    testdata_long = [(30, nullcontext(30)),
                     (pomo.inv.MIN_LONG-1, pytest.raises(ValueError, match="long")),
                     (pomo.inv.MAX_LONG+1, pytest.raises(ValueError, match="long")),
                     (pomo.inv.MIN_LONG, nullcontext(pomo.inv.MIN_LONG)),
                     (pomo.inv.MAX_LONG,  nullcontext(pomo.inv.MAX_LONG)),
                     (30.1, pytest.raises(TypeError, match="long")),
                     (True, pytest.raises(TypeError, match="long"))]
    
    @pytest.mark.parametrize("long,expected", testdata_long)
    def test_long_param(self, long, expected):
        with expected as e:
            res = pomo.create_interval_plan(long = long)
            assert res[-1].duration == e


    testdata_count = [(6, nullcontext(12)),
                     (pomo.inv.MIN_COUNT-1, pytest.raises(ValueError, match="count")),
                     (pomo.inv.MAX_COUNT+1, pytest.raises(ValueError, match="count")),
                     (pomo.inv.MIN_COUNT, nullcontext(pomo.inv.MIN_COUNT*2)),
                     (pomo.inv.MAX_COUNT,  nullcontext(pomo.inv.MAX_COUNT*2)),
                     (6.7, pytest.raises(TypeError, match="count")),
                     (True, pytest.raises(TypeError, match="count"))]
    
    @pytest.mark.parametrize("count,expected", testdata_count)
    def test_count_len(self, count, expected):
        with expected as e:
            res = pomo.create_interval_plan(n = count)
            assert len(res) == e

    def test_count_n1(self):
        res = pomo.create_interval_plan(n = 1)
        assert res == [pomo.Interval(pomo.IntervalType.WORK, 25,1), pomo.Interval(pomo.IntervalType.LONG, 20,1)]