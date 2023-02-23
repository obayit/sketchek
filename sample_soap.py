from zeep import Client as ZeepClient
from zeep.exceptions import Fault
from requests import Session
from pprint import pprint

SOAP_URL = 'http://www.dneonline.com/calculator.asmx?WSDL'

def do_stuff():
    client = ZeepClient(SOAP_URL)
    requestParams = {
        'intA': 1,
        'intB': 1,
    }
    try:
        print(requestParams)
        result = client.Add.getCitizenInfo(requestParams)
        print(result)
    except Fault as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
        print('ex')
        print(ex)
    return



