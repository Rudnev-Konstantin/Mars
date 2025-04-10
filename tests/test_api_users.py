def test_users(client):
    response = client.get("api/users")
    
    assert response.status_code == 200
    data = response.json
    assert isinstance(data["users"], list)
    assert len(data["users"]) == 1
    assert all("id" in user for user in data["users"])

def test_user(client):
    response = client.get("api/users/1")
    assert response.status_code == 200
    data = response.json
    assert isinstance(data["user"], dict)
    assert "id" in data["user"]
    
    response = client.get("api/users/0")
    assert response.status_code == 404
    assert "message" in response.json
    
    invalid_cases = ["abc", "1.5", "-1", "123abc"]
    for case in invalid_cases:
        response = client.get(f"api/users/{case}")
        assert response.status_code == 404

def test_create_user(client):
    # Тест успешного создания
    valid_data = {
        "surname": "Test",
        "name": "User",
        "age": 25,
        "speciality": "tester",
        "email": "test.email.test",
        "hashed_password": "hashed_password123"
    }
    response = client.post("/api/users", json=valid_data)
    assert response.status_code == 201
    assert "id" in response.json
    
    # Проверка создания
    user_id = response.json["id"]
    get_response = client.get(f"/api/users/{user_id}")
    assert get_response.status_code == 200
    assert get_response.json["user"]["id"] == user_id
    
    # Тест с отсутствующими полями
    invalid_data = {"name": "User"}
    response = client.post("/api/users", json=invalid_data)
    assert response.status_code == 400
    
    # Тест с неверными типами
    invalid_types = {
        "surname": "Test",
        "name": "User",
        "age": "not_a_number",
        "speciality": "tester",
        "email": "test_unique.email.test",
        "hashed_password": "hashed_password123"
    }
    response = client.post("/api/users", json=invalid_types)
    assert response.status_code == 400

def test_delete_user(client):
    response = client.delete("api/users/1")
    assert response.status_code == 200
    assert response.json["success"] == "OK"
    
    response = client.get("api/users/1")
    assert response.status_code == 404
    
    response = client.delete("api/users/0")
    assert response.status_code == 404
    assert "message" in response.json
    
    invalid_cases = ["abc", "1.5", "-1", "123abc"]
    for case in invalid_cases:
        response = client.delete(f"api/users/{case}")
        assert response.status_code == 404
