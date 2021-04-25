from src.providers import AirFreightCompanyRequest
import base64

user = {"login": "test", "pass": "passwordtest"}
userb64 = (
    base64.b64encode((user["login"] + ":" + user["pass"]).encode("ascii"))
).decode("ascii")
userb64_bad = (
    base64.b64encode((user["login"] + ":" + user["pass"]+"badddd").encode("ascii"))
).decode("ascii")

sales_rep_json = {
    "firstname": "Andres",
    "lastname": "Gonzales",
    "cell_phone": "+57 317 5386180",
    "email": "andres.gonzalez@finkargo.com",
}

sales_rep_json_2 = {
    "firstname": "Mark",
    "lastname": "Floyd",
    "cell_phone": "+1 317 5386180",
    "email": "mark.floyd@amazon.com",
}
air_freight_company_json = {
    "name": "Finkargo airline",
    "address": "Bogotá Colombia",
    "countries_wh_presence": ["Colombia", "México"],
    "sales_rep": sales_rep_json,
}

air_freight_company_json_2 = {
    "name": "Amazon airline",
    "address": "Miami United States",
    "countries_wh_presence": ["United States"],
    "sales_rep": sales_rep_json_2,
}

air_freight_company_request = AirFreightCompanyRequest(**air_freight_company_json)
air_freight_company_request_2 = AirFreightCompanyRequest(**air_freight_company_json_2)