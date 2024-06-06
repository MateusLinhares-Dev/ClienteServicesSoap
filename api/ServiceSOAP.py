import zeep
from zeep.transports import Transport
from zeep.exceptions import ValidationError, Fault
import requests

class ServiceClient:
    """
    Cliente para interação com um serviço SOAP utilizando autenticação JWT.

    Esta classe encapsula a lógica para se comunicar com um serviço SOAP por meio do protocolo HTTP.
    Utiliza a biblioteca Zeep para gerar e enviar solicitações SOAP, garantindo a autenticação
    através de um token JWT.

    Args:
        wsdl_url (str): URL do WSDL (Web Services Description Language) do serviço SOAP.
        service_url (str): URL do serviço SOAP.
        method_url (str): URL do método do serviço SOAP.
        jwt_token (str): Token JWT para autenticação.

    Attributes:
        wsdl_url (str): URL do WSDL do serviço SOAP.
        service_url (str): URL do serviço SOAP.
        method_url (str): URL do método do serviço SOAP.
        jwt_token (str): Token JWT para autenticação.
        client (zeep.Client): Cliente Zeep inicializado com transporte autenticado.
        header (zeep.xsd.Element): Elemento do cabeçalho SOAP.
    """
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

        # Criar o elemento do cabeçalho SOAP
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
        """ 
        Faz a chamada ao serviço SOAP.

        Este método é responsável por construir uma solicitação SOAP com os parâmetros fornecidos
        e enviá-la para o serviço SOAP. O método espera receber os parâmetros necessários para
        construir o corpo da solicitação SOAP.

        Args:
            **param: Parâmetros dinâmicos que serão passados para o método SOAP.
                Esses parâmetros são usados para construir o corpo da solicitação SOAP.

        Returns:
            response: A resposta do serviço SOAP.

        Raises:
            ValidationError: Se houver um erro de validação nos parâmetros.
            Fault: Se o serviço SOAP retornar uma falha.
        """
        # Construir o cabeçalho SOAP
        header_value = self.header(Action=self.method_url, To=self.service_url)

        try:
            # Enviar a solicitação SOAP para o serviço
            response = self.client.service.cancelWorkflow(
                _soapheaders=[header_value],
                **param
            )
            return response
        
        except ValidationError as val_err:
            # Lidar com erros de validação nos parâmetros
            value_err = str(val_err).split(' ')
            raise ValidationError(f"Parâmetro encaminhado é inválido - Parâmetro esperado: {value_err[2]} / ERRO: {val_err}")
            
        except Fault as f:
            # Lidar com falhas retornadas pelo serviço SOAP
            raise Fault(f)
