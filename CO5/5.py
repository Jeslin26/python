import csv
dict_columns = ['No','Name','Place']
dict_rows = [
{'No': 1, 'Name': 'ANJU', 'Place': 'Thrissur'},
{'No': 2, 'Name': 'BEENA', 'Place': 'Trivandrum'},
{'No': 3, 'Name': 'CHARU', 'Place': 'Kollam'},
{'No': 4, 'Name': 'DWANY', 'Place': 'Ernakulam'},
{'No': 5, 'Name': 'EMILY', 'Place': 'Kozhikode'},
]
with open('dict.csv', 'w') as csvwrite:
    writer = csv.DictWriter(csvwrite, fieldnames=dict_columns)
    writer.writeheader()
    writer.writerows(dict_rows)

n=0    
with open('dict.csv', 'r') as csvread:
    reader= csv.DictReader(csvread)
    for data in reader:
        if n==0:
            print(f'{"  ".join(data)}')
            n=n+1
        print(f'{data["No"]}{data["Name"]} {data["Place"]}' )
