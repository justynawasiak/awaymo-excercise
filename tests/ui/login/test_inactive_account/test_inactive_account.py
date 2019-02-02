import pytest

@pytest.mark.usefixtures("get_driver")
@pytest.mark.P1
@pytest.mark.tba
class TestInactiveAccount:
    def test_inactive_account(self):
        """
        Verify if user is able to log in with an inactive account.

        1. Open main page.
        2. Move to registration form.
        3. Confirm registration.
        4. Move to log in form.
        5. Provide e-mail address and password used during registration in 2nd form.
        6. Confirm logging in.

        Expected results:
        User shouldn't be able to log in as his account is inactive.
        Valid message should be displayed.
        """
