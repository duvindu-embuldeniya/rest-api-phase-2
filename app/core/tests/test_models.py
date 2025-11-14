"""
Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models."""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful."""
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        """exactly equal to the email you passed when creating the user"""
        self.assertEqual(user.email, email)
        
        """password you gave was correctly hashed and saved -> returns True"""
        self.assertTrue(user.check_password(password))
