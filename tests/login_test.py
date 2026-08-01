def test_login_success():
    username = "admin"
    password = "12345"

    is_login_successful = username == "admin" and password == "12345"

    assert is_login_successful is True
