import pytest

@pytest.mark.usefixtures("get_driver")
@pytest.mark.P4
@pytest.mark.manual
class TestGuiRegistrationForm:
    def test_gui_registration_form(self):
        """
        Check if registration form is implemented according to design.

        1. Check manually using design mocks.

        Expected results:
        <design_link>
        Registration form should have:
        - Required markings (during registration or after confirmation? - to be discussed)
        - Valid colors.
        - Valid behaviour on hover (changed color, background, pointer? - to be discussed).
        """
