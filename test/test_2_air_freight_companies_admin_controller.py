import pytest
from .mock_injector import mock_injector
from src.app import application
from flask.testing import FlaskClient
from flask import Response
from .constants import air_freight_company_json, air_freight_company_json_2
import json


@pytest.fixture
def client():
    app = application(dev=False, injector=mock_injector)
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_air_freight_companies_create(client: FlaskClient):
    response: Response = client.post(
        "admin/airfreightcompanies",
        data=json.dumps(air_freight_company_json),
        follow_redirects=True,
        content_type="application/json",
    )
    # happy case
    assert response != None and response.status_code == 200
    assert (
        response != None
        and isinstance(response.get_json(), dict)
        and response.get_json()["status"] == 200
        and response.get_json()["data"] != None
        and response.get_json()["data"]["id"] != None
        and response.get_json()["data"]["name"] == air_freight_company_json["name"]
    )
    # bad data
    bad_air_freight_company_json_copy = air_freight_company_json.copy()
    del bad_air_freight_company_json_copy["sales_rep"]
    response_bad: Response = client.post(
        "admin/airfreightcompanies",
        data=json.dumps(bad_air_freight_company_json_copy),
        follow_redirects=True,
        content_type="application/json",
    )
    assert (
        response_bad != None
        and response_bad.status_code == 400
        and isinstance(response_bad.get_json(), dict)
        and response_bad.get_json()["status"] == 400
        and response_bad.get_json()["error"] == "invalid_data"
    )


def test_air_freight_companies_update(client: FlaskClient):
    response_create: Response = client.post(
        "admin/airfreightcompanies",
        data=json.dumps(air_freight_company_json),
        follow_redirects=True,
        content_type="application/json",
    )
    air_freight_company_update = response_create.get_json()["data"].copy()
    air_freight_company_update["name"] = "Finkargo airline global"
    response_update: Response = client.put(
        "admin/airfreightcompanies",
        data=json.dumps(air_freight_company_update),
        follow_redirects=True,
        content_type="application/json",
    )
    # happy case
    assert (
        response_update != None
        and response_update.status_code == 200
        and response_update.get_json()["status"] == 200
        and response_update.get_json()["data"]["name"]
        == air_freight_company_update["name"]
    )
    # not found
    air_freight_company_update["id"] = "bad_keyu"
    response_not_found: Response = client.put(
        "admin/airfreightcompanies",
        data=json.dumps(air_freight_company_update),
        follow_redirects=True,
        content_type="application/json",
    )
    assert (
        response_not_found != None
        and response_not_found.status_code == 400
        and response_not_found.get_json()["status"] == 400
        and response_not_found.get_json()["error"] == "not_found"
    )
    # bad data
    air_freight_company_update["id"] = response_create.get_json()["data"]["id"]
    del air_freight_company_update["name"]
    response_invalid_data: Response = client.put(
        "admin/airfreightcompanies",
        data=json.dumps(air_freight_company_update),
        follow_redirects=True,
        content_type="application/json",
    )
    assert (
        response_invalid_data != None
        and response_invalid_data.status_code == 400
        and response_invalid_data.get_json()["status"] == 400
        and response_invalid_data.get_json()["error"] == "invalid_data"
    )


def test_air_freight_companies_get_one(client: FlaskClient):
    response_create: Response = client.post(
        "admin/airfreightcompanies",
        data=json.dumps(air_freight_company_json),
        follow_redirects=True,
        content_type="application/json",
    )
    air_freight_company_create = response_create.get_json()["data"].copy()
    response_get_one: Response = client.get(
        "admin/airfreightcompanies/" + air_freight_company_create["id"],
        follow_redirects=True,
    )
    # happy case
    assert (
        response_get_one != None
        and response_get_one.status_code == 200
        and response_get_one.get_json()["status"] == 200
        and response_get_one.get_json()["data"] != None
        and response_get_one.get_json()["data"]["id"]
        == air_freight_company_create["id"]
    )
    # not found
    response_not_found: Response = client.get(
        "admin/airfreightcompanies/not-found", follow_redirects=True
    )
    assert (
        response_not_found != None
        and response_not_found.status_code == 400
        and response_not_found.get_json()["status"] == 400
        and response_not_found.get_json()["error"] == "not_found"
    )


def test_air_freight_companies_delete(client: FlaskClient):
    response_create: Response = client.post(
        "admin/airfreightcompanies",
        data=json.dumps(air_freight_company_json),
        follow_redirects=True,
        content_type="application/json",
    )
    air_freight_company_create = response_create.get_json()["data"].copy()
    # happy case
    response_delete = client.delete(
        "admin/airfreightcompanies/" + air_freight_company_create["id"],
        follow_redirects=True,
    )
    assert (
        response_delete != None
        and response_delete.status_code == 200
        and response_delete.get_json()["status"] == 200
        and response_delete.get_json()["data"] == True
    )
    # not found
    response_delete_not_found = client.delete(
        "admin/airfreightcompanies/" + air_freight_company_create["id"],
        follow_redirects=True,
    )
    assert (
        response_delete_not_found != None
        and response_delete_not_found.status_code == 400
        and response_delete_not_found.get_json()["status"] == 400
        and response_delete_not_found.get_json()["error"] == "not_found"
    )


def test_air_freight_companies_search(client: FlaskClient):
    response_create: Response = client.post(
        "admin/airfreightcompanies",
        data=json.dumps(air_freight_company_json_2),
        follow_redirects=True,
        content_type="application/json",
    )
    air_freight_company_create = response_create.get_json()["data"].copy()
    response_search: Response = client.get(
        "admin/airfreightcompanies",
        query_string={"filter": "Amazon"},
        follow_redirects=True,
    )
    # happy case
    assert (
        response_search != None
        and response_search.status_code == 200
        and response_search.get_json()["status"] == 200
        and type(response_search.get_json()["data"]) is list
        and len(response_search.get_json()["data"]) == 1
    )
