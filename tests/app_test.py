import pytest
from src.app import app

# This is a "fixture"
# It sets up a "test client" for us to use
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# This is our first test function
def test_home_page_status_code(client):
    # 1. "client.get('/')" is like visiting the homepage
    response = client.get('/')
    
    # 2. We assert that the status code MUST be 200
    assert response.status_code == 200
# This is our second test function
def test_home_page_content(client):
    response = client.get('/')
    # We assert that the text "My To-Do List" is on the page
    # The 'b' is for "bytes", which is how Python handles web data
    assert b"My To-Do List" in response.data