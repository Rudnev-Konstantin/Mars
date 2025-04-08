def test_jobs(client):
    response = client.get("api/jobs")
    
    assert response.status_code == 200
    data = response.json
    assert isinstance(data["jobs"], list)
    assert len(data["jobs"]) == 2
    assert all("id" in job for job in data["jobs"])

def test_job(client):
    response = client.get("api/jobs/1")
    assert response.status_code == 200
    data = response.json
    assert isinstance(data["job"], dict)
    assert "id" in data["job"]
    
    response = client.get("api/jobs/0")
    assert response.status_code == 404
    assert response.json["error"] == "Not found"
    
    response = client.get("api/jobs/str")
    assert response.status_code == 404
    assert response.json["error"] == "Not found"

def test_create_job(client):
    # Тест успешного создания
    valid_data = {
        "team_leader": 1,
        "job": "Test job",
        "work_size": 10,
        "collaborators": "2,3",
        "is_finished": False
    }
    response = client.post("/api/jobs", json=valid_data)
    assert response.status_code == 201
    assert "id" in response.json
    
    # Проверка создания
    job_id = response.json["id"]
    get_response = client.get(f"/api/jobs/{job_id}")
    assert get_response.status_code == 200
    assert get_response.json["job"]["id"] == job_id
    
    # Тест с отсутствующими полями
    invalid_data = {"team_leader": 1}
    response = client.post("/api/jobs", json=invalid_data)
    assert response.status_code == 400
    
    # Тест с неверными типами
    invalid_types = {
        "team_leader": "not_a_number",
        "job": "Test",
        "work_size": 10,
        "collaborators": "2,3",
        "is_finished": False
    }
    response = client.post("/api/jobs", json=invalid_types)
    assert response.status_code == 400
