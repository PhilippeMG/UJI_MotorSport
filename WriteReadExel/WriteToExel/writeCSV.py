import pandas as pd

data = {'first_name': ['Sigrid', 'Joe', 'Theodoric', 'Kennedy', 'Beatrix', 'Olimpia', 'Grange', 'Sallee'],
        'last_name': ['Mannock', 'Hinners', 'Rivers', 'Donnell', 'Parlett', 'Guenther', 'Douce', 'Johnstone'],
        'age': [27, 31, 36, 53, 48, 36, 40, 34],
        'amount_1': [7.17, 1.90, 1.11, 1.41, 6.69, 4.62, 1.01, 4.88],
        'amount_2': [8.06, 3, 5.90, 4, 5, 7.48, 4.37, 7]}
df = pd.DataFrame(data, columns=['first_name', 'last_name', 'age', 'amount_1', 'amount_2'])
df.to_csv('example.csv' ,sheet_name='motor')
print("Creant el fitxer: example.csv")


#https://www.analyticslane.com/2018/06/15/guardar-y-leer-archivos-csv-con-python/

# fitxer="dades.csv"
# csv=open(fitxer,"a")
# info="Phil, Gonzalez, 24, 3.33, 9,99\n"
# i=0
# for i in range (5):
#         csv.write(info)