from func import open_json_file, filter_list, sort_operation_list, hide_from, hide_to, date_converting

# считывет файл
data = open_json_file('operations.json')

# фильтрует, оставляя только выполненные операции, и сортирует их по дате
data = sort_operation_list(filter_list(data))


#производит вывод 5 последних операций
for i in data[:5]:
    print(f'{date_converting(i.get("date"))} {i.get("description")}')
    print(f'{hide_from(i.get("from"))} -> {hide_to(i.get("to"))}')
    print(f'{i["operationAmount"].get("amount")} {i["operationAmount"]["currency"].get("name")}\n')