import csv
import json

def read_csv(file_name):
    data = {}
    with open(file_name, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            for key, value in row.items():
                if key is not None:
                    cleaned_key = key.strip().strip('"')
                    cleaned_value = value.strip()
                    if cleaned_key in data:
                        data[cleaned_key].append(cleaned_value)
                    else:
                        data[cleaned_key] = [cleaned_value]
    return data

def print_csv_data(data):
    for key, values in data.items():
        print(f'{key} -> {values}')

def min_column(data, column):
    values = list(map(float, data[column]))
    return min(values)

def max_column(data, column):
    values = list(map(float, data[column]))
    return max(values)

def sum_column(data, column):
    values = list(map(float, data[column]))
    return sum(values)

def avg_column(data, column):
    values = list(map(float, data[column]))
    return sum(values) / len(values)

def read_json(file_name):
    with open(file_name, mode='r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def write_json(data, file_name):
    with open(file_name, mode='w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def filter_users(data, query):
    filtered_data = [user for user in data if user['name'].split()[0].startswith(query)]
    return filtered_data

csv_data = read_csv('9.csv')
print_csv_data(csv_data)
print("Available columns:", csv_data.keys())

print("Min value (Age):", min_column(csv_data, 'Age'))
print("Max value (Age):", max_column(csv_data, 'Age'))
print("Sum (Age):", sum_column(csv_data, 'Age'))
print("Average value (Age):", avg_column(csv_data, 'Age'))

json_data = read_json('lab.json')
filtered_json_data = filter_users(json_data, 'Cha')
write_json(filtered_json_data, 'out.json')

print("Filtered JSON data has been written to 'out.json'")
