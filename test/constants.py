from src.providers import AirFreightCompanyRequest

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