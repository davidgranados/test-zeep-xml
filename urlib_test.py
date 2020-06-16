from builtins import breakpoint
from uu import decode

import chardet
import urllib3
import xmltodict


def guess_encoding(text):
    CODECS_LIST = [
        "ascii",
        "big5",
        "big5hkscs",
        "cp037",
        "cp273",
        "cp424",
        "cp437",
        "cp500",
        "cp720",
        "cp737",
        "cp775",
        "cp850",
        "cp852",
        "cp855",
        "cp856",
        "cp857",
        "cp858",
        "cp860",
        "cp861",
        "cp862",
        "cp863",
        "cp864",
        "cp865",
        "cp866",
        "cp869",
        "cp874",
        "cp875",
        "cp932",
        "cp949",
        "cp950",
        "cp1006",
        "cp1026",
        "cp1125",
        "cp1140",
        "cp1250",
        "cp1251",
        "cp1252",
        "cp1253",
        "cp1254",
        "cp1255",
        "cp1256",
        "cp1257",
        "cp1258",
        "euc_jp",
        "euc_jis_2004",
        "euc_jisx0213",
        "euc_kr",
        "gb2312",
        "gbk",
        "gb18030",
        "hz",
        "iso2022_jp",
        "iso2022_jp_1",
        "iso2022_jp_2",
        "iso2022_jp_2004",
        "iso2022_jp_3",
        "iso2022_jp_ext",
        "iso2022_kr",
        "latin_1",
        "iso8859_2",
        "iso8859_3",
        "iso8859_4",
        "iso8859_5",
        "iso8859_6",
        "iso8859_7",
        "iso8859_8",
        "iso8859_9",
        "iso8859_10",
        "iso8859_11",
        "iso8859_13",
        "iso8859_14",
        "iso8859_15",
        "iso8859_16",
        "johab",
        "koi8_r",
        "koi8_t",
        "koi8_u",
        "kz1048",
        "mac_cyrillic",
        "mac_greek",
        "mac_iceland",
        "mac_latin2",
        "mac_roman",
        "mac_turkish",
        "ptcp154",
        "shift_jis",
        "shift_jis_2004",
        "shift_jisx0213",
        "utf_32",
        "utf_32_be",
        "utf_32_le",
        "utf_16",
        "utf_16_be",
        "utf_16_le",
        "utf_7",
        "utf_8",
        "utf_8_sig",
    ]
    for best_enc in CODECS_LIST:
        try:
            text.encode(encoding=best_enc, errors="strict")
        except UnicodeEncodeError:
            pass
        else:
            return best_enc


def decode_persona_data_with_errors(personas):
    """Decode persona data to utf-8."""
    # errors = {"encode": {}, "decode": {}}
    for persona in personas:
        for key, value in persona.items():
            if value is not None:
                # try:
                persona.update(
                    {key: value.encode("windows-1252").decode("utf-8").lower()}
                )
                # except UnicodeEncodeError:
                #     if errors["encode"].get(persona["EMPLID"]) is None:
                #         errors["encode"].update({persona["EMPLID"]: []})
                #     errors["encode"][persona["EMPLID"]].append(
                #         {"key": key, "value": value}
                #     )
                # except UnicodeDecodeError:
                #     if errors["decode"].get(persona["EMPLID"]) is None:
                #         errors["decode"].update({persona["EMPLID"]: []})
                #     errors["decode"][persona["EMPLID"]].append(
                #         {"key": key, "value": value}
                #     )

        return personas


def decode_persona_data(personas):
    """Decode persona data to utf-8."""
    errors = {"encode": {}, "decode_after_encode": {}, "else_decode": {}}
    for persona in personas:
        for key, value in persona.items():
            if value is not None:
                # try:
                encode_value = value.encode("latin_1").decode("utf-8")
                # except UnicodeEncodeError:
                #     try:
                #         encode_value = value.encode("latin_1")
                #     except UnicodeEncodeError:
                #         if errors["encode"].get(persona["EMPLID"]) is None:
                #             errors["encode"].update(
                #                 {persona["EMPLID"]: []}
                #             )
                #         errors["encode"][persona["EMPLID"]].append(
                #             {"key": key, "value": value}
                #         )
                # else:
                    # try:
                    # persona.update({key: encode_value.decode("utf-8").lower()})
                    # except UnicodeDecodeError:
                    #     if errors["else_decode"].get(persona["EMPLID"]) is None:
                    #         errors["else_decode"].update(
                    #             {persona["EMPLID"]: []}
                    #         )
                    #     errors["else_decode"][persona["EMPLID"]].append(
                    #         {"key": key, "value": value}
                    #     )

    return personas, errors


http = urllib3.PoolManager()

# Construct xml payload to invoke the service. In the example, it is a hard coded string.
envelope = """<soap-env:Envelope xmlns:soap-env="http://schemas.xmlsoap.org/soap/envelope/">
                <soap-env:Body>
                    <ns0:EC_INFPROFNV_REQ_MSG xmlns:ns0="http://xmlns.oracle.com/Enterprise/Tools/schemas/EC_INFPROFNV_REQ_MSG.v1">
                            <ns0:INFPROFNV_REQ_MSG>
                            <ns1:EC_INFPRFNV_REQ xmlns:ns1="http://xmlns.oracle.com/Enterprise/Tools/schemas/INFPROFNV_REQ_PARC_MSG.v1">
                            </ns1:EC_INFPRFNV_REQ>
                        </ns0:INFPROFNV_REQ_MSG>
                    </ns0:EC_INFPROFNV_REQ_MSG>
                </soap-env:Body>
            </soap-env:Envelope>"""

# Create request for the service call
r = http.request_encode_body(
    "POST",
    "http://45.239.88.42:8200/PSIGW/PeopleSoftServiceListeningConnector/EC_IB_INFPROFNV_NB_SRV.1.wsdl",
    body=envelope,
    headers={
        "Content-Type": "application/xml",
        "SOAPAction": "EC_IB_INFPROFNV_NB_OPR.v1",
    },
)

webservice_response = xmltodict.parse(r.data)

personas = webservice_response["soapenv:Envelope"]["soapenv:Body"][
    "EC_INFPROFNV_NBRES_NBMSG"
]["EC_INFPROFNV_NBREQ_PR_NBMSG"]

personas = [persona["EC_INFPRNV_RSNB"] for persona in personas]


personas, errors = decode_persona_data(personas)

for persona in personas:
    print(persona)
