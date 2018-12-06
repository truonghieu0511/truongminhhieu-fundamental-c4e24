name_list =[
    {
        "name": "Huy",
        "VNDperhour":20,
        "hour":25,
    },
    {
        "name": "Huy",
        "VNDperhour":30,
        "hour":30,
    },
    {
        "name": "H.Duc",
        "VNDperhour":25,
        "hour":15,
    }
]
# s=0

# for i in name_list:
#     # print("tong luong",i["name"],i["VNDperhour"] * i["hour"])
#     name = i["name"]
#     vnd = i["VNDperhour"]
#     hour = i["hour"]
#     wage = vnd * hour
#     print(name,wage)
#     s = s + wage
# print("tong luong " , s)

wage_list = [p["VNDperhour"]*p["hour"] for p in name_list]
total = sum(wage_list)
print(total)
