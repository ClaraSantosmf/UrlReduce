# Create your tests here.
from devpro.encurtador.models import UrlRedirect


def test_redireciondor_sem_http(client, db):
    UrlRedirect.objects.create(destino='www.buser.com.br', slug='buser')
    response = client.get('/buser')
    assert response.url == 'http://www.buser.com.br'


def test_redireciondor_com_http(client, db):
    UrlRedirect.objects.create(destino='https://www.buser.com.br', slug='buser')
    response = client.get('/buser')
    assert response.url == 'https://www.buser.com.br'
