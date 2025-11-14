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
        name = 'testname'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            name=name,
            password=password,
        )
        """exactly equal to the email you passed when creating the user"""
        self.assertEqual(user.email, email)

        """password you gave was correctly hashed and saved -> returns True"""
        self.assertTrue(user.check_password(password))




    def test_new_user_email_normalized(self):
        """Test email is normalized for new users."""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.com', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'duvindu', 'sample123')
            self.assertEqual(user.email, expected)
