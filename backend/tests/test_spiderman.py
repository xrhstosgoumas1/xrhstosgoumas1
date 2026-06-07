import os
import requests

BASE_URL = os.environ.get('REACT_APP_BACKEND_URL', 'https://web-slinger-db-1.preview.emergentagent.com').rstrip('/')
SECTIONS = ["origin", "powers", "villains", "allies", "suits", "movies", "comics"]


def test_root_welcome():
    r = requests.get(f"{BASE_URL}/api/", timeout=15)
    assert r.status_code == 200
    data = r.json()
    assert "message" in data and "Spider-Man" in data["message"]


def test_get_all_returns_seven_keys():
    r = requests.get(f"{BASE_URL}/api/spiderman/all", timeout=15)
    assert r.status_code == 200
    data = r.json()
    for key in SECTIONS:
        assert key in data, f"missing key: {key}"
    # validate counts
    assert len(data["powers"]) == 6
    assert len(data["villains"]) == 6
    assert len(data["allies"]) == 6
    assert len(data["suits"]) == 4
    assert len(data["movies"]) == 6
    assert len(data["comics"]) == 7
    assert len(data["origin"]["paragraphs"]) >= 3
    # validate movie embed urls present
    for m in data["movies"]:
        assert m["embed_url"].startswith("https://www.youtube.com/embed/")


def test_each_section_endpoint():
    for s in SECTIONS:
        r = requests.get(f"{BASE_URL}/api/spiderman/{s}", timeout=15)
        assert r.status_code == 200, f"{s} failed: {r.status_code}"
        body = r.json()
        assert body["section"] == s
        assert "data" in body


def test_invalid_section_returns_404():
    r = requests.get(f"{BASE_URL}/api/spiderman/nonexistent", timeout=15)
    assert r.status_code == 404


def test_villain_images_reachable():
    r = requests.get(f"{BASE_URL}/api/spiderman/villains", timeout=15)
    villains = r.json()["data"]
    imgs = [v for v in villains if v.get("image")]
    assert len(imgs) >= 3
    # Images are served by frontend (static assets); construct absolute URL
    for v in imgs:
        url = v["image"] if v["image"].startswith("http") else f"{BASE_URL}{v['image']}"
        head = requests.get(url, timeout=15, stream=True)
        assert head.status_code == 200, f"{v['name']} image broken: {head.status_code}"
