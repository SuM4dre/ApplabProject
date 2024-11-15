import json
import boto3
from boto3.dynamodb.conditions import Attr

def lambda_handler(event, context):
    # Verificar el método HTTP utilizado en la solicitud
    method = event['httpMethod']
    
    # Verificar la ruta de la solicitud
    path = event['path']

    if method == 'GET' and path == '/buscar':
        query = event['queryStringParameters'].get('query', '')

        # Configurar DynamoDB
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('Productos')

        # Buscar productos en DynamoDB
        response = table.scan(
            FilterExpression=Attr('Nombre').contains(query)
        )

        resultados = response.get('Items', [])

        # Devolver la respuesta con los productos encontrados
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(resultados)
        }

    # Si la solicitud no coincide con el método y ruta esperados, devolver un error
    return {
        'statusCode': 400,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({'message': 'Solicitud no válida'})
    }
