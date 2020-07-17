from django.test import TestCase

from labcoffee.models import Author


class AuthorTests(TestCase):

    def test_new_author(self):
        autor = Author(first_name='Zé', last_name='Silva',
                       email='ze@silva.com', organizacao='Zé Corp')

        self.assertEqual(autor.first_name, 'Zé', 'Testa Nome')
        self.assertEqual(autor.last_name, 'Silva', 'Testa Sobrenome')
        self.assertEqual(str(autor), 'Zé Silva - Zé Corp', 'Testa Nome')
