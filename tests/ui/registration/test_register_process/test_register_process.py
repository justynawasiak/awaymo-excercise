import pytest

@pytest.mark.usefixtures("get_driver")
@pytest.mark.P1
@pytest.mark.tba
class TestRegisterProcess:
    def test_register_process(self):
        """
        Verify if user is able to register.

        1. Open main page.
        2. Move to registration form.
        3. Fill in all required fields with valid data.
        4. Confirm registration.

        Expected results:
        User should be redirected to confirmation page (to be discussed during grooming).
        User should receive an e-mail confirmation with a link.
        User shouldn't be activated after registration.
        """
