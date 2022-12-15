import unittest

from laboratorios.models import Laboratorio
from laboratorios.views import Laboratorio                                                                                                                 

class TestLaboratorio(unittest.TestCase):

    def setUp(self):
        self.laboratorio = Laboratorio()

    def test_criar(self):
        # Testa a criação de um novo registro no laboratório
        self.laboratorio.create("Exemplo de registro")
        self.assertEqual(len(self.laboratorio.registros), 1)

    def test_ler(self):
        self.laboratorio.criar("Exemplo de registro")
        registro = self.laboratorio.ler(0)
        self.assertEqual(registro, "Exemplo de registro")

    def test_atualizar(self):
        self.laboratorio.criar("Exemplo de registro")
        self.laboratorio.atualizar(0, "Novo exemplo de registro")
        registro = self.laboratorio.ler(0)
        self.assertEqual(registro, "Novo exemplo de registro")

    def test_apagar(self):
        self.laboratorio.criar("Exemplo de registro")
        self.laboratorio.apagar(0)
        self.assertEqual(len(self.laboratorio.registros), 0)