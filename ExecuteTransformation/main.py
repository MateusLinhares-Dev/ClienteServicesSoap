import sys
import os

from dotenv import load_dotenv

try:
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    # IMPORT SERVICE CLIENT ZEEP
    from api.GetWorkflow import ServiceClient

except ModuleNotFoundError:
    raise ModuleNotFoundError.__notes__

# Carregar variáveis de ambiente
load_dotenv()

# Configurações da URL e Token
wsdl_url = os.getenv('wsdl_url')
service_url = os.getenv('service_url')
method_url = os.getenv('method_url')
jwt_token = os.getenv('jwt_token')

# Criar o cliente do serviço com o JWT
client = ServiceClient(wsdl_url=wsdl_url, service_url=service_url, method_url=method_url, jwt_token=jwt_token)

# ID do workflow
workflow_id = os.getenv('workflow_id')
user_id = os.getenv('user_id')
explanation = os.getenv('explanation')

#Identificadores e valores para requisição soap
values = {
    "WorkflowID": workflow_id,
    "UserID": user_id,
    "Explanation": explanation,
}

response = client.call_service(**values)

print(response)
