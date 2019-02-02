import pytest

@pytest.mark.usefixtures("get_driver")
@pytest.mark.P1
@pytest.mark.tba
class TestActiveAccount:
    def test_active_account(self):
        """
        Verify if user is able to log in with an active account.

        1. Open main page.
        2. Move to registration form.
        3. Confirm registration.
        4. Activate account via link in email message.
        5. Move to log in form.
        6. Provide e-mail address and password used during registration in 2nd form.
        7. Confirm logging in.

        Expected results:
        User should be properly logged in.
        User should be redirected to his account page (to be discussed).
        """
