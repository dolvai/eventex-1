from django.core import mail
from django.test import TestCase


class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(name="Anderson Nunes", cpf="12345678901",
                    email="anderson@email.com", phone="11-988888888")
        self.response = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscript_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'anderson@email.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Anderson Nunes',
            '12345678901',
            'anderson@email.com',
            '11-988888888',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
