import urllib2
import base64


username = "username"
password = "password"

# Construct xml payload to invoke the service. In the example, it is a hard coded string.
envelope = """<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
                             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                             xmlns:xsd="http://www.w3.org/2001/XMLSchema">
                <soap:Body>
                 <findRule
                             xmlns="http://xmlns.oracle.com/apps/incentiveCompensation/cn/creditSetup/creditRule/creditRuleService/types/">
                    <findCriteria>
                        <fetchStart xmlns="http://xmlns.oracle.com/adf/svc/types/">0</fetchStart>
                        <fetchSize xmlns="http://xmlns.oracle.com/adf/svc/types/">-1</fetchSize>
                        <filter xmlns="http://xmlns.oracle.com/adf/svc/types/">
                            <group>
                               <upperCaseCompare>false</upperCaseCompare>
                               <item>
                                  <upperCaseCompare>false</upperCaseCompare>
                                  <attribute>RuleId</attribute>
                                  <operator>=</operator>
                                  <value>300000000851162</value>
                               </item>
                            </group>
                        </filter>
                        <excludeAttribute
                            xmlns="http://xmlns.oracle.com/adf/svc/types/">false</excludeAttribute>
                    </findCriteria>
                    <findControl>
                       <retrieveAllTranslations
                            xmlns="http://xmlns.oracle.com/adf/svc/types/">false</retrieveAllTranslations>
                    </findControl>
                 </findRule>
                </soap:Body>
            </soap:Envelope>"""

# Construct the base 64 encoded string used as credentials for the service call
credentials = base64.encodebytes("%s:%s" % (username, password))[:-1]
authorization = "Basic %s" % credentials

# Create and register opener. Requires proxy when behind a firewall
opener = urllib2.build_opener(
    urllib2.HTTPHandler(),
    urllib2.HTTPSHandler(),
    urllib2.ProxyHandler({"https": "proxyhost:proxyport"}),
)
urllib2.install_opener(opener)

# Create request for the service call
request = urllib2.Request(
    "https://host:port/icCnSetupCreditRulesPublicService/CreditRuleService"
)

# Configure the request content type to be xml
request.add_header("Content-Type", "text/xml;charset=UTF-8")

# Configure the request authentication in the header with base64-encoded user name and password
request.add_header("Authorization", authorization)

# Set the SOAP action to be invoked; while the call works without this, the value is expected to be set based on standards
request.add_header(
    "SOAPAction",
    "http://xmlns.oracle.com/apps/incentiveCompensation/cn/creditSetup/creditRule/creditRuleService/findRule",
)

# Write the xml payload to the request
request.add_data(envelope)

# Execute the request
handle = urllib2.urlopen(request)

# Get the response and process it. This example just prints the response.
content = handle.read()
print(content)
