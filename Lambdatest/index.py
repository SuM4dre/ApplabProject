import json

def lambda_handler(event, context):
    # Verificar el método HTTP utilizado en la solicitud
    method = event['httpMethod']
    
    # Verificar la ruta de la solicitud
    path = event['path']
    
    if method == 'GET' and path == '/buscar':
        query = event['queryStringParameters'].get('query', '')
        
        # Aquí agregarías la lógica para buscar productos en tu base de datos
        # Esto es solo un ejemplo
        productos = {
            "Productos": [
                {
                    "PutRequest": {
                        "Item": {
                            "ProductoID": {"S": "P001"},
                            "Nombre": {"S": "Achiote"},
                            "Descripcion": {"S": "El achiote condimento Mexicano, no es todavía un ingrediente muy conocido, cuando en realidad resulta básico en una despensa latinoamericana bien surtida, y no solo de México, los beneficios que se atribuyen a este ingrediente lo señalan como beneficioso para la digestión y para evitar problemas estomacales, aunque en realidad no hay estudios que avalen propiedades milagrosas de su consumo, sí es beneficioso en tanto a que ayuda a dar sabor y color apetitoso a los alimentos, con un aroma ligeramente ahumado y un punto picante pero muy ligero, siendo por tanto adecuado para personas de digestiones sensibles o que no toleren mucho la comida excesivamente condimentada, además, como todas las especias, ayuda a reducir el abuso de sal"},
                            "Precio": {"N": "25000"}
                        }
                    }
                },
                {
                    "PutRequest": {
                        "Item": {
                            "ProductoID": {"S": "P008"},
                            "Nombre": {"S": "Almendra"},
                            "Descripcion": {"S": "La almendra es un fruto seco que aportan diversos beneficios para la salud, pues ayuda a regular el azúcar en la sangre, previene la osteoporosis, ayuda a aumentar el colesterol HDL y favorece la ganancia de masa muscular, estos beneficios de las almendras se deben a que son ricas en fibras, proteínas y grasas saludables, además, también son ricas en antioxidantes, como taninos, flavonoides y vitamina E, por lo que ayudan a combatir el exceso de radicales libres en el organismo y previenen el surgimiento de diversas enfermedades, conozca otros alimentos ricos en antioxidantes."},
                            "Precio": {"N": "32000"}
                        }
                    }
                },
                {
                    "PutRequest": {
                        "Item": {
                            "ProductoID": {"S": "P018"},
                            "Nombre": {"S": "Arandanos"},
                            "Descripcion": {"S": "Los Arándanos deshidratados son arándanos frescos que han sido secados mediante un proceso de deshidratación. El proceso de deshidratación implica eliminar la humedad de la fruta y esto se hace generalmente mediante la exposición al sol o mediante el uso de calor o aire forzado. Los arándanos deshidratados son una forma muy popular de preservar y transportar la fruta. Además, son una forma muy práctica de disfrutar de los beneficios para la salud de los arándanos en cualquier momento y en cualquier lugar, ya que se pueden llevar fácilmente a cualquier lugar, Son una excelente fuente de antioxidantes,Pueden mejorar la salud del corazón,Pueden mejorar la salud del cerebro,Pueden ayudar a prevenir infecciones del tracto urinario.Los arándanos deshidratados son una excelente fuente de nutrientes y contienen muchas propiedades beneficiosas para la salud. Pueden ayudar a prevenir enfermedades, mejorar la función cerebral y la salud del corazón, y tienen propiedades antiinflamatorias y antimicrobianas. Si bien su consumo es seguro en cantidades moderadas, se debe tener precaución si se tienen ciertos problemas médicos como diabetes o problemas gastrointestinales. En general, agregar arándanos deshidratados a tu dieta es una forma fácil y deliciosa de mejorar tu salud y tu bienestar."},
                            "Precio": {"N": "32000"}
                        }
                    }
                }
            ]
        }
        
        # Filtrar productos según la consulta de búsqueda
        resultados = [producto["PutRequest"]["Item"] for producto in productos["Productos"] if query.lower() in producto["PutRequest"]["Item"]["Nombre"]["S"].lower()]

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
    