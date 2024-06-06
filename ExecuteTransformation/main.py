import sys
import os

from dotenv import load_dotenv

try:
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    # IMPORT SERVICE CLIENT ZEEP
    from api.ServiceSOAP import ServiceClient

except ModuleNotFoundError:
    raise ModuleNotFoundError.__notes__

def StructResponse(wsdl_url, service_url, method_url, jwt_token):
    """
    Estrutura e envia uma solicitação SOAP para um serviço utilizando um cliente Zeep.

    Esta função é responsável por criar um cliente para um serviço SOAP utilizando a biblioteca Zeep,
    construir uma solicitação SOAP com base nos valores fornecidos e enviá-la ao serviço.

    Args:
        wsdl_url (str): URL do WSDL (Web Services Description Language) do serviço SOAP.
        service_url (str): URL do serviço SOAP.
        method_url (str): URL do método do serviço SOAP.
        jwt_token (str): Token JWT para autenticação.

    Raises:
        ModuleNotFoundError: Se ocorrer um erro ao importar o módulo ServiceClient.

    Instructions:
        Antes de executar esta função, é necessário configurar as variáveis de ambiente no arquivo .env.
        Recomenda-se utilizar o pacote `python-dotenv` para carregar as variáveis de ambiente de forma segura.
        Crie um arquivo .env na raiz do seu projeto e defina as seguintes variáveis:
        
        - wsdl_url: URL do WSDL do serviço SOAP.
        - service_url: URL do serviço SOAP.
        - method_url: URL do método do serviço SOAP.
        - jwt_token: Token JWT para autenticação.
        - workflow_id: ID do workflow.
        - user_id: ID do usuário.
        - explanation: Explicação para a solicitação SOAP.
        
        Certifique-se de instalar o pacote `python-dotenv` usando o comando `pip install python-dotenv`.
        Em seguida, carregue as variáveis de ambiente usando `load_dotenv()` no seu script Python.

    """
    # Criar o cliente do serviço com o JWT
    client = ServiceClient(wsdl_url=wsdl_url, service_url=service_url, method_url=method_url, jwt_token=jwt_token)

    # ID do workflow obtido do ambiente
    workflow_id = os.getenv('workflow_id')
    user_id = os.getenv('user_id')
    explanation = os.getenv('explanation')

    # Identificadores e valores para a requisição SOAP
    values = {
        "WorkflowID": workflow_id,
        "UserID": user_id,
        "Explanation": explanation,
    }

    # Chamar o serviço SOAP com os valores fornecidos
    response = client.call_service(**values)

    # Imprimir a resposta do serviço
    print(response)


# Carregar variáveis de ambiente
load_dotenv()

# Configurações da URL e Token
wsdl_url = os.getenv('wsdl_url')
service_url = os.getenv('service_url')
method_url = os.getenv('method_url')
jwt_token = os.getenv('jwt_token')

# Chamar a função StructResponse com os valores configurados
StructResponse(wsdl_url, service_url, method_url, jwt_token)