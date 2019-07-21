import pandas as pd

data = {'first_name': ['Sigrid', 'Joe', 'Theodoric', 'Kennedy', 'Beatrix', 'Olimpia', 'Grange', 'Sallee'],
        'last_name': ['Mannock', 'Hinners', 'Rivers', 'Donnell', 'Parlett', 'Guenther', 'Douce', 'Johnstone'],
        'age': [27, 31, 36, 53, 48, 36, 40, 34],
        'amount_1': [7.17, 1.90, 1.11, 1.41, 6.69, 4.62, 1.01, 4.88],
        'amount_2': [8.06, "?", 5.90, "?", "?", 7.48, 4.37, "?"]}
df = pd.DataFrame(data, columns=['first_name', 'last_name', 'age', 'amount_1', 'amount_2'])
df.to_excel('excel.xlsx', sheet_name='motor')
print("Creant el fitxer: excel.xslx")


# import pandas as pd
# from pandas import ExcelWriter
#
# df = pd.DataFrame({'Id': [1, 3, 2, 4],
#                    'Nombre': ['Juan', 'Eva', 'María', 'Pablo'],
#                    'Apellido': ['Méndez', 'López', 'Tito', 'Hernández']})
# df = df[['Id', 'Nombre', 'Apellido']]
# writer = ExcelWriter('ejemplo.xlsx')
# df.to_excel(writer, 'Hoja de datos', index=False)
# writer.save()