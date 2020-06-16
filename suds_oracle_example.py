import base64
from suds.client import Client


url = "http://45.239.88.42:8200/PSIGW/PeopleSoftServiceListeningConnector/EC_IB_INFPROFNV_NB_SRV.1.wsdl"

headers = {
    "SOAPAction": "EC_IB_INFPROFNV_NB_OPR.v1",
}

# Create new client
client = Client(url=url, headers=headers)
print(client)

# INFPROFNV_REQ_MSG = client.factory.create("ns3:INFPROFNV_REQ_MSG_TypeShape")

# personal = client.service.EC_IB_INFPROFNV_NB_OPR(INFPROFNV_REQ_MSG)

# print(personal)
