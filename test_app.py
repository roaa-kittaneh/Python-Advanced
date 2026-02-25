from app import app

client = app.test_client()

def test_homepage():
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to Flask Student Portal" in response.data

def test_students_page():
    response = client.get('/students')
    assert response.status_code == 200
    assert b"Registered Students" in response.data