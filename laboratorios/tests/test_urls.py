from django.test import SimpleTestCase
from django.urls import reverse, resolve
from laboratorios.views import laboratorio_list, laboratorio_detail, LaboratorioCreateView


class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('laboratorio_list')
        print(resolve(url))
        self.assertEqual(resolve(url).func, laboratorio_list)

    def test_add_url_is_resolved(self):
        url = reverse('laboratorio_add')
        print(resolve(url))
        self.assertEqual(resolve(url).func, LaboratorioCreateView.as_view)

    def test_detail_url_is_resolved(self):
        url = reverse('laboratorio_detail', args=['some-slug'])
        print(resolve(url))
        self.assertEqual(resolve(url).func, laboratorio_detail)
