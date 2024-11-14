import yaml

def validate_yaml(file_path):
    try:
        with open(file_path, 'r') as stream:
            yaml.safe_load(stream)
        print(f"El archivo {file_path} es válido.")
    except yaml.YAMLError as exc:
        print(f"Error en el archivo YAML: {exc}")

# Ruta al archivo productos.yaml
validate_yaml('productos.yaml')
