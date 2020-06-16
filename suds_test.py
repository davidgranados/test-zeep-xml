"""Suds test."""
import logging
from suds.client import Client

# logging.basicConfig(level=logging.DEBUG)
# logging.getLogger('suds.client').setLevel(logging.DEBUG)

url = "http://45.239.88.42:8200/PSIGW/PeopleSoftServiceListeningConnector/EC_IB_INFPROFNV_NB_SRV.1.wsdl"
client = Client(url)

INFPROFNV_REQ_MSG = client.factory.create("ns3:INFPROFNV_REQ_MSG_TypeShape")
INFPROFNV_REQ_MSG.EC_INFPRFNV_REQ.EMPLID = "80039484"
# INFPROFNV_REQ_MSG.EC_INFPRFNV_REQ._class = "xsd:string"

client.service.EC_IB_INFPROFNV_NB_OPR(INFPROFNV_REQ_MSG)
