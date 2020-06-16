from zeep import Client

client = Client(wsdl="http://www.dneonline.com/calculator.asmx?WSDL")

print(client.service.Add(10, 10))
