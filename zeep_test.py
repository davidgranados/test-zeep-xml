"""SOAP Client test."""
from zeep import Client, Settings
from lxml import etree
from zeep import Plugin


# class MyLoggingPlugin(Plugin):
#     def ingress(self, envelope, http_headers, operation):
#         print(etree.tostring(envelope, pretty_print=True))
#         return envelope, http_headers

#     def egress(self, envelope, http_headers, operation, binding_options):
#         print(etree.tostring(envelope, pretty_print=True))
#         return envelope, http_headers


settings = Settings(force_https=False)
client = Client(
    "http://45.239.88.42:8200/PSIGW/PeopleSoftServiceListeningConnector/EC_IB_INFPROFNV_NB_SRV.1.wsdl",
    # settings=settings, plugins=[MyLoggingPlugin()]
)

INFPROFNV_REQ_MSG = client.get_type("ns1:INFPROFNV_REQ_MSG_TypeShape")
EC_INFPRFNV_REQ = client.get_type("ns1:EC_INFPRFNV_REQMsgDataRecord_TypeShape")
EC_INFPRFNV_REQ_OBJ = EC_INFPRFNV_REQ("80039484", "xsd:string")
INFPROFNV_REQ_MSG_OBJ = INFPROFNV_REQ_MSG(EC_INFPRFNV_REQ_OBJ)
client.service.EC_IB_INFPROFNV_NB_OPR(INFPROFNV_REQ_MSG_OBJ)
# client.service.EC_IB_INFPROFNV_NB_OPR()
