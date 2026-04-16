from backend.app import create_app
import json

app = create_app()
client = app.test_client()
resp = client.post('/auth/register', json={'username':'testuser','email':'test@example.com','password':'password123'})
print('status', resp.status_code)
print(resp.get_data(as_text=True))
