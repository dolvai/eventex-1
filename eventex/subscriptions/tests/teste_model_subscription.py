from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
                name="Anderson Nunes", cpf="12345678901",
                email="anderson@email.com", phone="11-988888888")
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription mus have an auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Anderson Nunes', str(self.obj))

    def test_paid_default_to_false(self):
        """By default, paid must be false"""
        self.assertEqual(False, self.obj.paid)
