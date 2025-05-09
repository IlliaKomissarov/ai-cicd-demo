def test_home_page(client):
    """Test the home page response."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to the AI CI/CD Demo' in response.data

def test_non_existent_page(client):
    """Test a non-existent page response."""
    response = client.get('/non-existent')
    assert response.status_code == 404