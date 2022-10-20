import pytest
from fastapi.testclient import TestClient
from app.main import app
import os
from testcontainers.core.container import DockerContainer

client = TestClient(app=app)


@pytest.mark.integration
def test_create_post(mongodb_instance):
    # when
    response = client.get("/")
    # then
    assert response.status_code == 200
    assert response.json() == {"message": "hello"}


@pytest.fixture(scope='session', autouse=True)
def mongodb_instance():
    with DockerContainer(image='mongo:latest') as mongo:
        mongo\
            .with_env('MONGO_INITDB_ROOT_USERNAME', 'test_app')\
            .with_env('MONGO_INITDB_ROOT_PASSWORD', 'test_password')\
            .with_env('MONGO_INITDB_DATABASE', 'test-app')\
            .with_exposed_ports('27017')
        update_mysql_config(mongo)
        mongo.start()
        yield mongo
        mongo.stop()


def update_mysql_config(mongodb):
    os.environ['MONGO_URL'] = mongodb.get_connection_url()
