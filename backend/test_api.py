import requests

# Test de registro
print("=== TEST DE REGISTRO ===")
response = requests.post(
    'http://localhost:8000/api/auth/registro/',
    json={
        'username': 'testuser2',
        'email': 'test2@example.com',
        'password': 'password123'
    }
)
print(f"Status: {response.status_code}")
print(f"Response: {response.text}")

# Test de login
print("\n=== TEST DE LOGIN ===")
response = requests.post(
    'http://localhost:8000/api/auth/login/',
    json={
        'username': 'testuser2',
        'password': 'password123'
    }
)
print(f"Status: {response.status_code}")
print(f"Response: {response.text}")