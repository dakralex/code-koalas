import csv
import pandas as pd

def cyclists_per_month (csv_file):
    my_count = []
    
    for line in csv_file:
        
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        
        cyclist_count = 0
        
        for i,row in enumerate(csv_reader):
            
            if int(i) == 0:
                line_count+=1
                continue
            
            rowCount = 0
            for j in row:
                if rowCount == 0:
                    rowCount += 1
                    continue
                
            
                if (j == ""): continue
                cyclist_count += int(j)
                rowCount += 1

            if ((int(i)-1)%730 == 0):
                if(int(i) == 1): continue
                my_count.append(cyclist_count)
                cyclist_count = 0                

            line_count += 1
            
            
    return my_count
    


file2018 = open('data2018.csv')
file2019 = open('data2019.csv')
file2020 = open('data2020.csv')
file2021 = open('data2021.csv')
file2022 = open('data2022.csv')
file2023 = open('data2023.csv')

cyclists_per_month_result = []

cyclists_per_month_result.append(cyclists_per_month(file2018))
cyclists_per_month_result.append(cyclists_per_month(file2019))
cyclists_per_month_result.append(cyclists_per_month(file2020))
cyclists_per_month_result.append(cyclists_per_month(file2021))
cyclists_per_month_result.append(cyclists_per_month(file2022))
cyclists_per_month_result.append(cyclists_per_month(file2023))

years = [2018, 2019, 2020, 2021, 2022, 2023]
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

data = [["year","month","count"]]

count = 1
for i in range(0,6):
    for j in cyclists_per_month_result[i]:
        data.append([years[i]])
        data[count].append(months[i])
        data[count].append(j)
        
        count += 1

print(data)


with open("result.csv", mode='w', newline='') as file:
    # Create a csv.writer object
    wrter = csv.writer(file)
    # rite data to the CSV file
    wrter.writerows(data)


csv_file = pd.DataFrame(pd.read_csv("result.csv", sep = ",", header = 0,encoding ='utf-8'))

csv_file.to_json("cyclists.json", orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)