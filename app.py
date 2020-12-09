import pandas as pd
import re
import os
garchivo = "data/TRNBCB_2017_03.txt"
''' print(os.getcwd()) '''
# para sacar el nombrecito del archivo excel oe
nombrecito = garchivo[-11:-4]

dfGarchivo = pd.read_csv(garchivo, sep='\t', names=['prueba'])
dfGarchivo['prueba'] = dfGarchivo['prueba'].str.replace(",", ".")
dfGarchivo.drop(
    dfGarchivo[dfGarchivo['prueba'].str[-16:] == '0000000000000.00'].index, inplace=True)
''' print(dfGarchivo.head(10)) '''
data = {
    # 'Emisor': dfGarchivo['prueba'].str[9:12],
    # 'Adquiriente': dfGarchivo['prueba'].str[12:15],
    'TipoTarjeta': dfGarchivo['prueba'].str[15:16],
    'Sucursal': dfGarchivo['prueba'].str[16:19],
    # 'Marca': dfGarchivo['prueba'].str[19:20],
    'Anio': dfGarchivo['prueba'].str[20:22],
    'Mes': dfGarchivo['prueba'].str[22:24],
    'Dia': dfGarchivo['prueba'].str[24:26],
    # 'Moneda': dfGarchivo['prueba'].str[26:28],
    'Importe': dfGarchivo['prueba'].str[-16:],
}
dfPatrabajar = pd.DataFrame(data)
dfPatrabajar['Importe'] = pd.to_numeric(
    dfPatrabajar['Importe'], errors='coerce')
''' Resumen = dfPatrabajar.groupby(
    ['Sucursal', 'TipoTarjeta', 'Anio', 'Mes', 'Dia']).agg({'Importe': ['sum', 'count', 'median', 'mean', 'min', 'max']})
with pd.ExcelWriter(nombrecito + '.xlsx') as writer:  # pylint: disable=abstract-class-instantiated
    Resumen.to_excel(writer, sheet_name='Resumen') '''
print(dfPatrabajar.size)
# para exportar a un excel
''' dfPatrabajar.to_excel(nombrecito + '.xlsx') '''
