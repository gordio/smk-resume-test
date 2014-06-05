from django.test import TestCase
from .forms import SignupFormExtra


class SignInTests(TestCase):
    """
    User sign in form
    """

    def test_correct_data(self):
        form_data = {
            'username': "myusername",
            'password1': "123456",
            'password2': "123456",
            'email': "user@mail.local",
            'first_name': "FirstName",
            'last_name': "LastName",
            'burn_date': "1999-01-01",
            'mob_phone': "(420) 555-1234",
        }
        form = SignupFormExtra(data=form_data)
        # FIXME: Ignore captcha
        self.assertTrue(form.is_valid())

    def test_required_data(self):
        # response = self.client.post("/accounts/signin", {'foo': 'bar'})
        # self.assertFormError(response, 'form', 'foo', 'This field is required.')
        pass


    def test_error_data(self):
        pass
