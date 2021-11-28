import pytest
from requests import get, post
from datetime import datetime

@pytest.fixture
def reqres_url1():
    return get('https://reqres.in/api/unknown/2')

@pytest.fixture
def reqres_url2():
    return post('https://reqres.in/api/users', {"name": "IIM","job": "superhero"})

def test_get_singleresource_statuscode(reqres_url1):
    res = reqres_url1
    assert res.status_code == 200

def test_get_singleresource_len(reqres_url1):
    res = reqres_url1
    assert len(res.json()) == 2

def test_get_singleresource_dataid(reqres_url1):
    res = reqres_url1
    res_body = res.json()
    assert res_body["data"]["id"] == 2

# ---
def test_post_create_status(reqres_url2):
    res = reqres_url2
    assert res.status_code == 201

def test_post_create_date(reqres_url2):
    res = reqres_url2
    date_formatted =  datetime.strptime(res.json()['createdAt'], "%Y-%m-%dT%H:%M:%S.%fZ")
    assert date_formatted.year == datetime.now().year
