import json
import pathlib
import pandas as pd
from termcolor import cprint

def json_to_csv(file_name):
    if pathlib.Path(file_name).exists():
        cprint(f'El archivo {file_name} existe, se procede a convertirlo a csv', 'green')
        with open(file_name, 'r', encoding='utf-8') as file_json:
            data = json.load(file_json)

        df = pd.json_normalize(data, record_path=['register', 'facultades', 'carreras', 'materias'],
                               meta=[['register','universidad'],
                                     ['register','ubicacion'],
                                     ['register','facultades', 'nombre'],
                                     ['register','facultades', 'carreras', 'nombre']],
                               errors='ignore')

        df.columns = ['Materia' ,'Creditos', 'Universidad', 'Ubicacion', 'Facultad', 'Carrera']
        df.to_csv('register_file.csv', index=False)
        cprint('register_file.csv creada exitosamente!', 'green')

    else:
        cprint(f'El archivo {file_name} no existe.', 'red')

def main():
    file_name = 'register.json'
    json_to_csv(file_name)

if __name__ == '__main__':
    main()