"""Requests test."""
import requests

url = "http://45.239.88.42:8200/PSIGW/PeopleSoftServiceListeningConnector/EC_IB_INFPROFNV_NB_SRV.1.wsdl"
headers = {
    "content-type": "text/xml",
    "SOAPAction": "EC_IB_INFPROFNV_NB_OPR.v1",
}
payload = """<soap-env:Envelope xmlns:soap-env="http://schemas.xmlsoap.org/soap/envelope/">
            <soap-env:Body>
                <ns0:EC_INFPROFNV_REQ_MSG xmlns:ns0="http://xmlns.oracle.com/Enterprise/Tools/schemas/EC_INFPROFNV_REQ_MSG.v1">
                        <ns0:INFPROFNV_REQ_MSG>
                        <ns1:EC_INFPRFNV_REQ xmlns:ns1="http://xmlns.oracle.com/Enterprise/Tools/schemas/INFPROFNV_REQ_PARC_MSG.v1">
                            <ns1:EMPLID>80039484</ns1:EMPLID>
                        </ns1:EC_INFPRFNV_REQ>
                    </ns0:INFPROFNV_REQ_MSG>
                </ns0:EC_INFPROFNV_REQ_MSG>
            </soap-env:Body>
        </soap-env:Envelope>"""
r = requests.post(url, data=payload, headers=headers, verify=False, stream=False)
print(r.contet)

# url = "http://wsf.cdyne.com/WeatherWS/Weather.asmx?WSDL"
# # headers = {'content-type': 'application/soap+xml'}
# headers = {"content-type": "text/xml"}
# body = """<?xml version="1.0" encoding="UTF-8"?>
#          <SOAP-ENV:Envelope xmlns:ns0="http://ws.cdyne.com/WeatherWS/" xmlns:ns1="http://schemas.xmlsoap.org/soap/envelope/"
#             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
#             <SOAP-ENV:Header/>
#               <ns1:Body><ns0:GetWeatherInformation/></ns1:Body>
#          </SOAP-ENV:Envelope>"""

# response = requests.post(url, data=body, headers=headers)
# print(response.content)
