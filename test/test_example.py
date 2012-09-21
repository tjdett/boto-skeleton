from nose.tools import eq_, ok_, raises

class TestExample:

    def test_ok(self):
        ok_(True)

    def test_eq(self):
        eq_(2 + 2, 4)

    @raises(TypeError, ValueError)
    def test_raises(self):
        raise TypeError("This is expected.")
