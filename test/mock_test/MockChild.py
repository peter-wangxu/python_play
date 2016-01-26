import mock


class MockTest(mock.Mock):

    def test_fun1(self, p1, p2):
        pass


m = MockTest()
m.test_fun1(1, 2)

m.test_fun1.assert_called_with(1, 2)