import py_compile


def test_app_syntax():
    py_compile.compile("app.py", doraise=True)
