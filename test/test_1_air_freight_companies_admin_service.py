from .mock_injector import mock_injector
from .constants import (
    air_freight_company_request,
    air_freight_company_json,
    air_freight_company_request_2,
)
from src.services import AirFreightCompanyAdminService
from src.providers import AirFreightCompanyRequest


service_instance: AirFreightCompanyAdminService = (
    mock_injector.air_freight_companies_admin_service()
)


def test_create_company():
    ok_data = service_instance.create(company_request=air_freight_company_request)
    # happy case
    assert ok_data != None and ok_data.id != None and ok_data.name == "Finkargo airline"
    # bad data
    try:
        local_json = air_freight_company_json.copy()
        del local_json["sales_rep"]
        updatecompany_bad_key = service_instance.create(
            company_request=AirFreightCompanyRequest(**local_json)
        )
    except ValueError as error:
        assert error.args[0] == "invalid_data"
    # none
    try:
        service_instance.create(company_request=None)
    except Exception as error:
        assert error.args[0] == "error"


def test_delete_company():
    create_company = service_instance.create(
        company_request=air_freight_company_request
    )
    # happy case
    delete_ok = service_instance.delete(str(create_company.id))
    assert delete_ok == True
    # bad key
    try:
        service_instance.delete(str("badkeyadsa"))
    except ValueError as error:
        assert error.args[0] == "not_found"
    # none
    try:
        service_instance.delete(id=None)
    except Exception as error:
        assert error.args[0] == "error"


def test_update_company():
    create_company = service_instance.create(
        company_request=air_freight_company_request
    )
    air_freight_company_json_copy = air_freight_company_json.copy()
    air_freight_company_json_copy["id"] = str(create_company.id)
    air_freight_company_json_copy["name"] = "Finkargo airline global"
    local_request = AirFreightCompanyRequest(**air_freight_company_json_copy)
    updatecompany_ok = service_instance.update(company_request=local_request)
    # happy case
    assert (
        updatecompany_ok != None and updatecompany_ok.name == "Finkargo airline global"
    )
    # bad key
    try:
        local_request.id = "bad-re-ba-key"
        updatecompany_bad_key = service_instance.update(company_request=local_request)
    except ValueError as error:
        assert error.args[0] == "not_found"
    # none value
    try:
        updatecompany_bad_key = service_instance.update(company_request=None)
    except Exception as error:
        assert error.args[0] == "error"


def test_search_company():
    create_company = service_instance.create(
        company_request=air_freight_company_request_2
    )
    data = service_instance.search(_filter="amazon")
    assert data != None and len(data) == 1
    empty_data = service_instance.search(_filter="finkargo not foyd")
    assert empty_data != None and len(empty_data) == 0