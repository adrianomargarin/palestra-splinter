# -*- coding:utf-8 -*-

from time import sleep

from splinter import Browser

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from apps.teste.utils import soma

User = get_user_model()


class TestSpliter(TestCase, StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super(TestSpliter, cls).setUpClass()
        # cls.browser = Browser("firefox")
        # cls.browser = Browser("phantomjs")

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super(TestSpliter, cls).tearDownClass()

    def setUp(self):
        self.create_superuser()

    def create_superuser(self):
        self.user = User.objects.create_superuser(username="adrianomargarin",
                                                  email="teste@exemplo.com",
                                                  password="123456")

    def login(self):
        self.browser.visit("%s%s" % (self.live_server_url, "/admin/login"))
        self.browser.fill_form({"username": "adrianomargarin",
                                "password": "123456"})
        button = self.browser.find_by_value("Log in")
        # sleep(5)
        button.click()

    def test_pesquisa_google(self):
        self.browser.visit("http://google.com")
        self.browser.fill("q", "splinter - python acceptance testing for web applications")
        button = self.browser.find_by_name("btnG")
        # sleep(5)
        button.click()
        # sleep(5)
        self.assertTrue(self.browser.is_text_present("splinter.readthedocs.org"))

    def test_login_admin_django(self):
        self.login()

        # sleep(5)
        self.assertTrue(self.browser.find_link_by_href("/admin/logout/"))

    def test_create_group(self):
        self.login()
        add = self.browser.find_link_by_href("/admin/auth/group/add/")
        # sleep(5)
        add.click()
        name = "Grupo 1"
        self.browser.fill_form({"name": name})
        # sleep(5)
        self.browser.find_by_name("_save").click()

        # sleep(5)
        self.assertEqual(Group.objects.first().name, name)

    def test_soma_focusout(self):
        self.browser.visit(self.live_server_url)

        valor1 = self.browser.find_by_name("valor1").first
        valor2 = self.browser.find_by_name("valor2").first
        resultado = self.browser.find_by_name("resultado").first

        # sleep(5)
        valor1.fill("2")
        # sleep(5)
        valor2.fill("2")

        # sleep(5)
        self.browser.evaluate_script("$('#id_valor2').focusout()")
        self.browser.screenshot()
        # sleep(5)
        self.assertEqual(resultado.value, '4')


class TestSoma(TestCase):

    def test_soma_dois_numeros_positivos(self):
        self.assertEqual(4, soma(2, 2))

    def test_soma_um_numero_positivo_com_um_negativo(self):
        self.assertEqual(0, soma(2, -2))

    def test_soma_dois_numeros_negativos(self):
        self.assertEqual(-4, soma(-2, -2))
