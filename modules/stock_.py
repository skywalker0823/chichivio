
import requests, json

def get_stock_data(stock_number_or_name):
    url = "https://openapi.twse.com.tw/v1/opendata/t187ap03_L"
    response = requests.get(url)
    response_list = json.loads(response.text)
    for company in response_list:
        if company['公司代號'] == stock_number_or_name or company['公司簡稱'] == stock_number_or_name or company['英文簡稱'].upper() == stock_number_or_name.upper():
            return {'status':'0','data':company}
    return {'status':'1'}