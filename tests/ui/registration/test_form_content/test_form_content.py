import pytest


@pytest.mark.usefixtures("get_driver")
@pytest.mark.P1
@pytest.mark.tba
class TestFormContent:
    def test_form_content(self):
        """
        Verify registration form's content.

        1. Open main page.
        2. Move to registration form.

        Expected result:
        Registration form should contain following fields:
        - first name,
        - last name,
        - email address,
        - password,
        - date of birth.
        and a confirmation button.
        """