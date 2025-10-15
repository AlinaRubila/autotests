import requests

api_url = "https://reqres.in/api"

def test_get():
    user_id = 1
    h = {"x-api-key": "reqres-free-v1"}
    response = requests.get(f"{api_url}/users/{user_id}", headers=h)

    #test for status code
    assert response.status_code == 200

    #test for structure
    data = response.json()
    assert "data" in data
    assert "id" in data["data"]
    assert "email" in data["data"]
    assert "first_name" in data["data"]
    assert "last_name" in data["data"]
    assert "avatar" in data["data"]

def test_post():
    name = "Alina"
    job = "student"
    body = {"name": name, "job": job}
    h = {"x-api-key":"reqres-free-v1"}
    response = requests.post(f"{api_url}/users", headers=h, json=body)

    #test for status code
    assert response.status_code == 201

    #test for structure
    data = response.json()
    assert "name" in data
    assert "job" in data
    assert "createdAt" in data

    #test for valid data
    assert data["name"] == name
    assert data["job"] == job

def test_put():
    name = "Anila"
    job = "student"
    user_id = 684
    body = {"name": name, "job": job}
    h = {"x-api-key":"reqres-free-v1"}
    response = requests.put(f"{api_url}/users/{user_id}", headers=h, json=body)

    #test for status code
    assert response.status_code == 200

    # test for structure
    data = response.json()
    assert "name" in data
    assert "job" in data
    assert "updatedAt" in data

    # test for valid data
    assert data["name"] == name
    assert data["job"] == job