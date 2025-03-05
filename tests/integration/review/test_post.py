from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_post_review(setup_db):
    json = {
        "restaurant_name": "ガスト",
        "nearest_station": "虎ノ門駅",
        "genres": [1, 2],
        "url": "https://linecorp.com",
        "comment": "まあまあ美味しい"
    }
    response = client.post("/review", json=json)
    assert response.status_code == 200
    assert response.json() == {"id": 1}
