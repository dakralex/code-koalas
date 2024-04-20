import pandas as pd

csv_file = pd.DataFrame(pd.read_csv("Verkehrsunfaelle_2018.csv", sep = ";", header = 0, encoding ='latin1'))
csv_file2 = pd.DataFrame(pd.read_csv("Verkehrsunfaelle_2019.csv", sep = ",", header = 0, encoding ='latin1'))
csv_file3 = pd.DataFrame(pd.read_csv("Verkehrsunfaelle_2020.csv", sep = ",", header = 0, encoding ='latin1'))
csv_file4 = pd.DataFrame(pd.read_csv("Verkehrsunfaelle_2021.csv", sep = ",", header = 0, encoding ='latin1'))
csv_file5 = pd.DataFrame(pd.read_csv("Verkehrsunfaelle_2022_part1.csv", sep = ";", header = 0, encoding ='latin1'))
csv_file6 = pd.DataFrame(pd.read_csv("Verkehrsunfaelle_2022_part2.csv", sep = ";", header = 0, encoding ='latin1'))

print("success")

filtered_csv = pd.concat([csv_file, csv_file2, csv_file3, csv_file4, csv_file5, csv_file6], axis=0, ignore_index=True)

filtered_csv = filtered_csv.query('IstRad==1')
filtered_csv = filtered_csv.drop('OBJECTID', axis=1)

#filtered_csv = filtered_csv.drop('LAND', axis=1)
#filtered_csv = filtered_csv.drop('BEZ', axis=1)
#filtered_csv = filtered_csv.drop('LOR', axis=1)
##filtered_csv = filtered_csv.drop('STRASSE', axis=1)
#filtered_csv = filtered_csv.drop('LOR_ab_2021', axis=1)
#filtered_csv = filtered_csv.drop('USTUNDE', axis=1)
#filtered_csv = filtered_csv.drop('UWOCHENTAG', axis=1)
#filtered_csv = filtered_csv.drop('UART', axis=1)
#filtered_csv = filtered_csv.drop('UTYP1', axis=1)
#filtered_csv = filtered_csv.drop('ULICHTVERH', axis=1)
#filtered_csv = filtered_csv.drop('IstPKW', axis=1)
#filtered_csv = filtered_csv.drop('IstFuss', axis=1)
#filtered_csv = filtered_csv.drop('IstKrad', axis=1)
#filtered_csv = filtered_csv.drop('IstGkfz', axis=1)
#filtered_csv = filtered_csv.drop('IstSonstig', axis=1)
#filtered_csv = filtered_csv.drop('STRZUSTAND', axis=1)
#filtered_csv = filtered_csv.drop('LINREFX', axis=1)
#filtered_csv = filtered_csv.drop('LINREFY', axis=1)

#filtered_csv = filtered_csv.drop('IstRad', axis=1)

filtered_csv = filtered_csv[['UJAHR','UMONAT','XGCSWGS84','YGCSWGS84','UKATEGORIE','IstPKW','IstFuss','IstKrad','IstSonstig']]

filtered_csv = filtered_csv.rename(columns = {'UJAHR': 'year', 'UMONAT': 'month','XGCSWGS84':'long', 'YGCSWGS84':'lat','UKATEGORIE': 'type', 'IstPKW' :'car', 'IstFuss': 'pedestrian', 'IstSonstig': 'other', 'IstKrad': 'motorcycle'})


#converts the strings with , to float types with .
filtered_csv['long'] = filtered_csv['long'].str.replace(',','.').astype('float')
filtered_csv['lat'] = filtered_csv['lat'].str.replace(',','.').astype('float')

filtered_csv['car'] = filtered_csv['car'].astype('bool')
filtered_csv['pedestrian'] = filtered_csv['pedestrian'].astype('bool')
filtered_csv['other'] = filtered_csv['other'].astype('bool')
filtered_csv['motorcycle'] = filtered_csv['motorcycle'].astype('bool')
filtered_csv['year'] = filtered_csv['year'].astype('int')
filtered_csv['month'] = filtered_csv['month'].astype('int')
filtered_csv['type'] = filtered_csv['type'].astype('int')




filtered_csv.to_json("plsWork.json", orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)

