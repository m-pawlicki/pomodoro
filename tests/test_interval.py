import pomodoro.interval as pomo
import pytest

class TestInterval:

    def test_default_pass(self):
        i = pomo.Interval()
        res = i.create_interval()
        assert res == [pomo.IntervalType.WORK, pomo.IntervalType.SHORT, pomo.IntervalType.WORK, pomo.IntervalType.SHORT, pomo.IntervalType.WORK, pomo.IntervalType.SHORT, pomo.IntervalType.WORK, pomo.IntervalType.LONG]

    #@pytest.mark.parametrize("work,expected", [(60)])


    def test_work_pass(self):
        i = pomo.Interval()
        res = i.create_interval(work=60)

    def test_work_range_fail(self):
        i = pomo.Interval()
        with pytest.raises(ValueError):
            i.create_interval(work=100)

    def test_work_edge_min(self):
        i = pomo.Interval()
        res = i.create_interval(work=pomo.inv.MIN_WORK)

    def test_work_edge_max(self):
        i = pomo.Interval()
        res = i.create_interval(work=pomo.inv.MAX_WORK)

    def test_work_type_float(self):
        i = pomo.Interval()
        with pytest.raises(TypeError):
            i.create_interval(work=5.5) #type: ignore

    def test_work_type_bool(self):
        i = pomo.Interval()
        with pytest.raises(TypeError):
            i.create_interval(work=True)

    def test_work_n0(self):
        i = pomo.Interval()
        with pytest.raises(ValueError):
            i.create_interval(work=0)


    def test_short_pass(self):
        i = pomo.Interval()
        res = i.create_interval(short=10)

    def test_short_range_fail(self):
        i = pomo.Interval()
        with pytest.raises(ValueError):
            i.create_interval(short=25)

    def test_short_edge_min(self):
        i = pomo.Interval()
        res = i.create_interval(short=pomo.inv.MIN_SHORT)

    def test_short_edge_max(self):
        i = pomo.Interval()
        res = i.create_interval(short=pomo.inv.MAX_SHORT)

    def test_short_type_float(self):
        i = pomo.Interval()
        with pytest.raises(TypeError):
            i.create_interval(short=6.9) #type: ignore

    def test_short_type_bool(self):
        i = pomo.Interval()
        with pytest.raises(TypeError):
            i.create_interval(short=False)

    def test_short_n0(self):
        i = pomo.Interval()
        with pytest.raises(ValueError):
            i.create_interval(short=0)


    def test_long_pass(self):
        i = pomo.Interval()
        res = i.create_interval(long=30)

    def test_long_range_fail(self):
        i = pomo.Interval()
        with pytest.raises(ValueError):
            i.create_interval(long=67)

    def test_long_edge_min(self):
        i = pomo.Interval()
        res = i.create_interval(long=pomo.inv.MIN_LONG)

    def test_long_edge_max(self):
        i = pomo.Interval()
        res = i.create_interval(long=pomo.inv.MAX_LONG)

    def test_long_type_float(self):
        i = pomo.Interval()
        with pytest.raises(TypeError):
            i.create_interval(long=42.0) #type: ignore

    def test_long_type_bool(self):
        i = pomo.Interval()
        with pytest.raises(TypeError):
            i.create_interval(long=True)

    def test_long_n0(self):
        i = pomo.Interval()
        with pytest.raises(ValueError):
            i.create_interval(long=0)


    def test_count_pass(self):
        i = pomo.Interval()
        res = i.create_interval(n=8)

    def test_count_range_fail(self):
        i = pomo.Interval()
        with pytest.raises(ValueError):
            i.create_interval(n=15)

    def test_count_edge_min(self):
        i = pomo.Interval()
        res = i.create_interval(n=pomo.inv.MIN_COUNT)

    def test_count_edge_max(self):
        i = pomo.Interval()
        res = i.create_interval(n=pomo.inv.MAX_COUNT)

    def test_count_type_float(self):
        i = pomo.Interval()
        with pytest.raises(TypeError):
            i.create_interval(n=5.5) #type: ignore

    def test_count_type_bool(self):
        i = pomo.Interval()
        with pytest.raises(TypeError):
            i.create_interval(n=False)

    def test_count_n1(self):
        i = pomo.Interval()
        res = i.create_interval(n=1)
        assert res == [pomo.IntervalType.WORK, pomo.IntervalType.LONG]

    def test_count_n0(self):
        i = pomo.Interval()
        with pytest.raises(ValueError):
            i.create_interval(n=0)