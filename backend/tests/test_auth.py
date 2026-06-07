"""Tests for JWT auth endpoints: /api/auth/register, /api/auth/login, /api/auth/me"""
import os
import uuid
import requests

BASE_URL = os.environ['REACT_APP_BACKEND_URL'].rstrip('/')
API = f"{BASE_URL}/api"


def _unique_email():
    return f"TEST_{uuid.uuid4().hex[:10]}@spidey.example.com"


# ---------- Register ----------

def test_register_success_returns_user_and_token():
    email = _unique_email()
    r = requests.post(f"{API}/auth/register", json={
        "email": email, "password": "webhead123", "name": "Test Spider"
    }, timeout=15)
    assert r.status_code == 200, r.text
    data = r.json()
    assert "token" in data and isinstance(data["token"], str) and len(data["token"]) > 20
    assert "user" in data
    assert data["user"]["email"] == email.lower()
    assert data["user"]["name"] == "Test Spider"
    assert "id" in data["user"]


def test_register_email_normalized_lowercase():
    raw = f"TEST_Upper_{uuid.uuid4().hex[:8]}@SPIDEY.EXAMPLE.COM"
    r = requests.post(f"{API}/auth/register", json={
        "email": raw, "password": "webhead123", "name": "Case Tester"
    }, timeout=15)
    assert r.status_code == 200
    assert r.json()["user"]["email"] == raw.lower()


def test_register_duplicate_email_returns_400():
    email = _unique_email()
    p = {"email": email, "password": "webhead123", "name": "Dup"}
    r1 = requests.post(f"{API}/auth/register", json=p, timeout=15)
    assert r1.status_code == 200
    r2 = requests.post(f"{API}/auth/register", json=p, timeout=15)
    assert r2.status_code == 400
    assert "already" in r2.json().get("detail", "").lower()


def test_register_short_password_returns_422():
    r = requests.post(f"{API}/auth/register", json={
        "email": _unique_email(), "password": "abc", "name": "Shorty"
    }, timeout=15)
    assert r.status_code == 422


def test_register_invalid_email_returns_422():
    r = requests.post(f"{API}/auth/register", json={
        "email": "not-an-email", "password": "webhead123", "name": "Bad"
    }, timeout=15)
    assert r.status_code == 422


# ---------- Login ----------

def test_login_success_returns_token():
    # Use seeded test user
    r = requests.post(f"{API}/auth/login", json={
        "email": "peter@queens.nyc", "password": "webhead123"
    }, timeout=15)
    assert r.status_code == 200, r.text
    data = r.json()
    assert data["user"]["email"] == "peter@queens.nyc"
    assert data["user"]["name"]
    assert isinstance(data["token"], str)


def test_login_email_case_insensitive():
    r = requests.post(f"{API}/auth/login", json={
        "email": "Peter@Queens.NYC", "password": "webhead123"
    }, timeout=15)
    assert r.status_code == 200
    assert r.json()["user"]["email"] == "peter@queens.nyc"


def test_login_wrong_password_returns_401():
    r = requests.post(f"{API}/auth/login", json={
        "email": "peter@queens.nyc", "password": "wrong-pass"
    }, timeout=15)
    assert r.status_code == 401


def test_login_nonexistent_email_returns_401():
    r = requests.post(f"{API}/auth/login", json={
        "email": "nobody-xyz@nope.example.com", "password": "whatever1"
    }, timeout=15)
    assert r.status_code == 401


# ---------- /auth/me ----------

def test_me_with_valid_token():
    login = requests.post(f"{API}/auth/login", json={
        "email": "peter@queens.nyc", "password": "webhead123"
    }, timeout=15)
    token = login.json()["token"]
    r = requests.get(f"{API}/auth/me",
                     headers={"Authorization": f"Bearer {token}"}, timeout=15)
    assert r.status_code == 200
    body = r.json()
    assert body["email"] == "peter@queens.nyc"
    assert "id" in body
    # ensure no password leaks
    assert "password_hash" not in body
    assert "password" not in body


def test_me_without_token_returns_401():
    r = requests.get(f"{API}/auth/me", timeout=15)
    assert r.status_code == 401


def test_me_with_bad_token_returns_401():
    r = requests.get(f"{API}/auth/me",
                     headers={"Authorization": "Bearer not.a.real.jwt"}, timeout=15)
    assert r.status_code == 401


def test_me_with_wrong_scheme_returns_401():
    r = requests.get(f"{API}/auth/me",
                     headers={"Authorization": "Token abc"}, timeout=15)
    assert r.status_code == 401


# ---------- Full register -> me flow ----------

def test_register_then_use_token_for_me():
    email = _unique_email()
    reg = requests.post(f"{API}/auth/register", json={
        "email": email, "password": "webhead123", "name": "Flow"
    }, timeout=15).json()
    token = reg["token"]
    me = requests.get(f"{API}/auth/me",
                      headers={"Authorization": f"Bearer {token}"}, timeout=15)
    assert me.status_code == 200
    assert me.json()["email"] == email.lower()
    assert me.json()["name"] == "Flow"
