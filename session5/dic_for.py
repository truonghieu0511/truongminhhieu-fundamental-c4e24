person = {
    "name":"H.Duc",
    "age": 25,
    "city": "Hanoi",
    "books": ["sapiens","tieu ngao giang ho ", "Tam quoc"]
}
print(person["name"])
print(person["books"])
# books = person["books"]
# print(books)
for b in person["books"]:
    print(b)
print(person["books"][1])
# print(books[-1])
# # for x in person:
#     print(x,person[x])
# for v in person.values():
#     print(v)
# for k,v in person.items():
#     print(k , v)
