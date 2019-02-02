import pytest

@pytest.mark.usefixtures("get_driver")
@pytest.mark.P2
@pytest.mark.tba
class TestEmailValidation:
    def test_email_validation(self):
        """
        Verify e-mail field validation during users registration.

        1. Open main page.
        2. Move to registration form.
        3. Provide invalid data in e-mail field:
        - simple text, ie 'user'
        - invalid format, ie 'wp.pl'
        - e-mail already existing
        4. Confirm registration.

        Expected result:
        User should still be on registration page.
        E-mail field should be marked with valid message.
        User should not receive e-mail registration message.
        """