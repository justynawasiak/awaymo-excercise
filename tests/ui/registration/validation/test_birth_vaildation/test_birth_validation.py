import pytest

@pytest.mark.usefixtures("get_driver")
@pytest.mark.P2
@pytest.mark.tba
class TestBirthValidation:
    def test_birth_validation(self):
        """
        Verify date of birth field validation during users registration. (- To be discussed, field may be not editable, value chosen only from calendar)

        1. Open main page.
        2. Move to registration form.
        3. Provide invalid data in date field:
        - simple text, ie 'birth'
        - invalid format, ie '2019 Jan 01'
        - other invalid formats, if applicable
        - date from the future, ie '01-01-2020'
        4. Confirm registration.

        Expected result:
        User should still be on registration page.
        Date of birth field should be marked with valid message.
        User should not receive e-mail registration message.
        """