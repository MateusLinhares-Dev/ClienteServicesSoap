import zeep
from zeep import Client
from zeep.transports import Transport
import requests

class ServiceClient:

    def __init__(self, wsdl_url, service_url, method_url, jwt_token):
        self.wsdl_url = wsdl_url
        self.service_url = service_url
        self.method_url = method_url
        self.jwt_token = jwt_token

        # Inicializar o transporte com cabeçalho de autenticação
        session = requests.Session()
        session.headers.update({'Authorization': f'{self.jwt_token}'})
        transport = Transport(session=session)

        # Inicializar o cliente Zeep com o transporte autenticado
        self.client = zeep.Client(wsdl=self.wsdl_url, transport=transport)

        # Criar o elemento do cabeçalho
        self.header = zeep.xsd.Element(
            "Header",
            zeep.xsd.ComplexType(
                [
                    zeep.xsd.Element(
                        "{http://www.w3.org/2005/08/addressing}Action", zeep.xsd.String()
                    ),
                    zeep.xsd.Element(
                        "{http://www.w3.org/2005/08/addressing}To", zeep.xsd.String()
                    ),
                ]
            ),
        )

    def call_service(self, **param):
        # Definir o valor do cabeçalho
        header_value = self.header(Action=self.method_url, To=self.service_url)

        """ Fazer a chamada ao serviço SOAP -
        client.service.cancelWorkflo -> método definido como cancelWorkflow atribui ao valor passado ao name da requisição 
        a ser efetuada -->  <operation name="cancelWorkflow">
        """
        response = self.client.service.cancelWorkflow(
            _soapheaders=[header_value],
            **param
        )
        return response

