# Consumindo Serviços SOAP com Python e Zeep

Neste projeto, estamos explorando a utilização da tecnologia SOAP (Simple Object Access Protocol) para se comunicar com serviços web. O SOAP é um protocolo de comunicação baseado em XML, comumente utilizado em sistemas distribuídos.

## Conceito

Nosso objetivo é criar uma estrutura flexível e reutilizável para consumir serviços SOAP em Python. Para isso, estamos utilizando a biblioteca Zeep, que facilita a criação de clientes SOAP em Python.

## Utilização do ServiceSOAP

O arquivo `ServiceSOAP.py` contém a lógica para se comunicar com serviços SOAP utilizando a classe `ServiceClient`. Esta classe encapsula a lógica de construção e envio de solicitações SOAP, além de lidar com a autenticação JWT.

Para consumir diferentes serviços SOAP, podemos reutilizar o `ServiceClient` alterando apenas o método e a URL do serviço desejado. Por exemplo, para consumir um serviço chamado `ServiceSOAP`, basta substituir a chamada `cancelWorkflow` por `GetWorkflow`.

## Exemplo de Uso

No arquivo `main.py`, podemos utilizar o `ServiceSOAP` para consumir diferentes serviços SOAP apenas alterando o método e a URL do serviço desejado. Por exemplo:

```python
from api.ServiceSOAP import ServiceClient

# Configurações para consumir o serviço ServiceSOAP
wsdl_url = "URL_DO_WSDL_DO_SERVICESOAP"
service_url = "URL_DO_SERVIÇO_DO_SERVICESOAP"
method_url = "URL_DO_MÉTODO_DO_SERVICESOAP"
jwt_token = "TOKEN_JWT_PARA_AUTENTICAÇÃO"

# Criar cliente para o serviço ServiceSOAP
client = ServiceClient(wsdl_url, service_url, method_url, jwt_token)

# Parâmetros para a requisição SOAP
params = {
    "param1": valor1,
    "param2": valor2,
    # Adicionar outros parâmetros, se necessário
}

# Chamar o serviço ServiceSOAP
response = client.call_service(**params)

print(response)
