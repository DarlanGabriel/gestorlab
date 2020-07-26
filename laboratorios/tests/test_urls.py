from django.test import SimpleTestCase
from django.urls import reverse, resolve
from laboratorios.views import laboratorio_list, laboratorio_detail, LaboratorioCreateView, home


class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('laboratorio_home')
        self.assertEqual(resolve(url).func, home)

    def test_list_url_is_resolved(self):
        url = reverse('laboratorio_list')
        self.assertEqual(resolve(url).func, laboratorio_list)

    def test_add_url_is_resolved(self):
        url = reverse('laboratorio_add')
        self.assertEqual(resolve(url).func.view_class, LaboratorioCreateView)

    def test_detail_url_is_resolved(self):
        url = reverse('laboratorio_detail', args=['some-slug'])
        self.assertEqual(resolve(url).func, laboratorio_detail)
