from datetime import datetime

from django.test import TestCase
import django
django.setup()
from labcoffee.models import Author, Presentation


class ModelTests(TestCase):

    def test_new_author(self):
        autor = Author(first_name='Zé', last_name='Silva',
                       email='ze@silva.com', organizacao='Zé Corp')

        self.assertEqual(autor.first_name, 'Zé', 'Testa Nome')
        self.assertEqual(autor.last_name, 'Silva', 'Testa Sobrenome')
        self.assertEqual(str(autor), 'Zé Silva - Zé Corp', 'Testa Nome')

    def test_new_presentation(self):
        apresentacao = Presentation(title='Usando Testes de Unidade', description='Testes de Unidade no Python',
                                    start_date=datetime.now, status='Planejado')
        autor = Author(first_name='Zé', last_name='Silva',
                       email='ze@silva.com', organizacao='Zé Corp')
        apresentacao.author = autor

        self.assertEqual(str(apresentacao), 'Usando Testes de Unidade (Zé Silva - Zé Corp)')
