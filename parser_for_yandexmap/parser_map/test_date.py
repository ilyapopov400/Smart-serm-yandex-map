data = [{'address': 'просп. имени В.И. Ленина, 54Б, Волгоград, РоссияТРК Европа Сити Молл', 'phone': None},
        {'address': 'просп. имени В.И. Ленина, 65К, Волгоград, РоссияТЦ Стройград', 'phone': None},
        {'address': 'бул. 30-летия Победы, 21, район Семь Ветров, ВолгоградТРК Парк Хаус, этаж 3',
         'phone': '8 (800) 600-77-75'}, {'address': 'Историческая ул., 154, ВолгоградТЦ Столплит хоум', 'phone': None},
        {'address': 'ул. Землячки, 110Б, Волгоград, Россияэтаж 1', 'phone': None}]

if __name__ == "__main__":
    for i in data:
        print("address: ", i["address"])
        print("phone: ", i["phone"])
