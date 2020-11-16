import pytest

class TestLogin:

    def setup_class(self):
        print('setup')

    @pytest.mark.run(order=2)
    def test_login(self):
        print('login')
        assert True

    @pytest.mark.run(order=1)
    def test_login2(self):
        print('login2')
        assert True

    @pytest.mark.skipif(True, reason='Skip')
    def test_login3(self):
        print('login3')
        assert True

    def teardown_class(self):
        print('teardown')

# if __name__ == '__main__':
#     pytest.main(['-s', 'D:\\PythonPractice\\pytestPractice\\pyt.py'])