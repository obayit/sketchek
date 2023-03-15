from zeep import Client as ZeepClient
from zeep.transports import Transport
from zeep.exceptions import Fault
from requests import Session
from pprint import pprint

SOAP_URL = 'http://www.dneonline.com/calculator.asmx?WSDL'

def do_stuff():
    session = Session()
    cert_path = '/opt/odoo/cert.pem'
    session.verify = cert_path
    transport = Transport(session=session)
    client = ZeepClient(SOAP_URL, transport=transport)
    try:
        result = client.service.Add(1, 1)
        print('result')
        print(result)
    except Fault as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
        print('ex')
        print(ex)
    return

do_stuff()

