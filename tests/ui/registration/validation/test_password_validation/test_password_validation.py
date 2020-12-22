import pytest


@pytest.mark.usefixtures("get_driver")
@pytest.mark.P2
@pytest.mark.tba
class TestPasswordValidation:
    def test_password_validation(self):
        """
        Verify password field validation during users registration.

        1. Open main page.
        2. Move to registration form.
        3. Provide invalid data in password field:
        - insufficient criteria, ie 'password', 'password1', 'Password', 'Pass1'
        4. Confirm registration.

        Expected result:
        User should still be on registration page.
        Password field should be marked with valid message.
        User should not receive e-mail registration message.
        """