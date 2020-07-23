from django.test import TestCase

from laboratorios.models import Laboratorio


class TestModels(TestCase):

    def test_model_laboratorio(self):

        lab1 = Laboratorio(nome='Laboratório 1', sigla='LAB1',
                           descricao='XXXXX')

        self.assertEqual(lab1.nome, 'Laboratório 1', 'T01 - Testa nome.')
