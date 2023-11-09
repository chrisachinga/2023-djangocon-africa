from django.test import TestCase
from .models import User

class UserTestCase(TestCase):
    def setUp(self):
        # Create a user instance for testing
        User.objects.create_user(
            username='testuser', 
            email='test@example.com', 
            password='testpassword', 
            phone_number='1234567890',
            gender='Male',
            year_of_birth=1990
        )

    def test_user_creation(self):
        """Test the user creation process."""
        user = User.objects.get(username='testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('testpassword'))
        self.assertFalse(user.is_verified)  # Default value is False

    def test_user_string_representation(self):
        """Test the user's string representation."""
        user = User.objects.get(username='testuser')
        self.assertEqual(str(user), 'testuser')

    def test_user_gender_field(self):
        """Test the gender field choices."""
        user = User.objects.get(username='testuser')
        self.assertIn(user.gender, [choice[0] for choice in User.GENDER_CHOICES])

    def test_user_phone_field(self):
        """Test the phone number field."""
        user = User.objects.get(username='testuser')
        self.assertEqual(user.phone_number, '1234567890')

    def test_user_year_of_birth_field(self):
        """Test the year of birth field."""
        user = User.objects.get(username='testuser')
        self.assertEqual(user.year_of_birth, 1990)
