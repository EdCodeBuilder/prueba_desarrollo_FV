# -*- coding: utf-8 -*-

import base64
import io
import os
import pandas as pd
from odoo import models, fields, api

class ExcelTransformer(models.Model):
    _name = 'excel.transformer'
    _description = 'Excel Transformer'

    excel_file = fields.Binary(string='Excel File')
    transformed_file = fields.Binary(string='Transformed File', readonly=True)
    filename = fields.Char(string='Filename')
    processed_filename = fields.Char(string='Processed Filename', readonly=True)

    @api.onchange('excel_file')
    def onchange_excel_file(self):
        if self.excel_file and not self.filename:
            filename, extension = os.path.splitext(self.excel_file.filename)
            self.filename = filename

    def process_excel_file(self):
        if self.excel_file:
            data = base64.b64decode(self.excel_file)
            df = pd.read_excel(io.BytesIO(data))

            # Definir las reglas de transformación
            reglas = [
                { 
                    "nombre": "ANIO",
                    "tipo": "NUMERICO",
                    "TAMANO": 4
                },
                { 
                    "nombre": "CONCEPTO",
                    "tipo": "ALFANUMERICO",
                    "TAMANO": 10
                },
                { 
                    "nombre": "VALOR",
                    "tipo": "NUMERICO",
                    "TAMANO": 20
                }
            ]

            # Convertir las reglas a un diccionario para facilitar su uso
            reglas_dict = {}
            for regla in reglas:
                reglas_dict[regla['nombre']] = regla

            # Aplicar las reglas de transformación a cada columna del DataFrame
            for col in df.columns:
                if col in reglas_dict:
                    regla = reglas_dict[col]
                    if regla['tipo'] == 'NUMERICO':
                        df[col] = df[col].apply(lambda x: str(int(x)).zfill(regla['TAMANO']) if pd.notna(x) else '')
                    elif regla['tipo'] == 'ALFANUMERICO':
                        df[col] = df[col].apply(lambda x: str(x)[:regla['TAMANO']].ljust(regla['TAMANO'], '$') if pd.notna(x) else '')
                    else:
                        pass
            
            # Convertir el DataFrame transformado a un archivo de texto
            output = io.StringIO()
            df.to_csv(output, index=False, header=False, sep=',', line_terminator='\n')

            # Eliminar la coma del archivo CSV generado
            output.seek(0)
            output_modified = io.StringIO()
            for line in output:
                line_modified = line.replace(',', '')
                output_modified.write(line_modified)
            
            # Guardar el archivo transformado y su nombre
            self.transformed_file = base64.b64encode(output_modified.getvalue().encode('utf-8'))
            filename2, extension = os.path.splitext(self.filename)
            self.processed_filename = filename2 + '_transformed.txt'
