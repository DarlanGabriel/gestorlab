from django.test import TestCase, Client
from django.urls import reverse
from laboratorios.models import Laboratorio, LinhaPesquisa


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('laboratorio_home')
        self.list_url = reverse('laboratorio_list')
        self.detail_url = reverse('laboratorio_detail', args=['labtest'])
        Laboratorio.objects.create(
            nome='labtest',
            sigla='labtest',
            descricao='fsfs sfsdv egwgw vfss'
        )

    def test_laboratorio_home_GET(self):
        response = self.client.get(self.home_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'laboratorios/laboratorio-list.html')

    def test_laboratorio_list_GET(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'laboratorios/laboratorio-list.html')

    def test_laboratorio_detail_GET(self):
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'laboratorios/laboratorio-detail.html')
