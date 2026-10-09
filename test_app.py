from app import app

def test_home():
    response = app.test_client().get("/")
    assert response.status_code == 200

def test_menu():
    response = app.test_client().get("/menu")
    assert response.status_code == 200

def test_order():
    response = app.test_client().get("/order")
    assert response.status_code == 200