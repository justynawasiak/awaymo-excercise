import pytest

@pytest.mark.usefixtures("get_driver")
@pytest.mark.P1
@pytest.mark.tba
@pytest.mark.issue
class TestFieldsRequired:
    def test_fields_required(self):
        """
        Verify if all fields are required during users registration.

        1. Open main page.
        2. Move to registration form.
        3. Confirm registration.

        Expected results:
        User should still be on registration page.
        All fields should be marked as required with valid messages (to be discussed during grooming).
        User should not receive e-mail registration message.
        """