import boto3
import yaml
from decimal import Decimal

# Cargar datos del archivo YAML
with open("productos.yaml", "r") as file:
    productos = yaml.safe_load(file)["productos"]

# Inicializar cliente de DynamoDB
dynamodb = boto3.resource('dynamodb')
tabla = dynamodb.Table('Productos')

# Función para convertir los precios a Decimal y asegurarse de que ProductoID esté presente
def convert_and_validate_item(product):
    if "ProductoID" not in product:
        raise ValueError("Falta la clave 'ProductoID' en el ítem")
    product["Precio"] = Decimal(str(product["Precio"]))
    return product

# Cargar datos en la tabla DynamoDB
for producto in productos:
    producto = convert_and_validate_item(producto)
    tabla.put_item(Item=producto)
    print(f"Cargado: {producto['ProductoID']} - {producto['Nombre']}")
