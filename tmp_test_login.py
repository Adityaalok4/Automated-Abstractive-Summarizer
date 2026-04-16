from backend.app import create_app

app = create_app()
client = app.test_client()

# Register a user
reg = client.post('/auth/register', json={'username':'ui_test','email':'ui_test@example.com','password':'password123'})
print('register status', reg.status_code)
print(reg.get_data(as_text=True))

# Attempt login with correct credentials
login = client.post('/auth/login', json={'username':'ui_test','password':'password123'})
print('login status', login.status_code)
print(login.get_data(as_text=True))

# Attempt login with wrong password
login_bad = client.post('/auth/login', json={'username':'ui_test','password':'wrong'})
print('login bad status', login_bad.status_code)
print(login_bad.get_data(as_text=True))
