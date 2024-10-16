from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app

client = TestClient(app)


def test_root_deve_retrnar_ok_e_ola_mundo():
    client = TestClient(app) # Cria um cliente de teste

    response = client.get('/') # Faz uma requisição GET para a rota '/'

    assert response.status_code == HTTPStatus.OK #Assert que o status code da resposta é 200
    assert response.json() == {'Hello': 'World'} #Assert que o conteúdo da resposta é {'Hello': 'World'}
