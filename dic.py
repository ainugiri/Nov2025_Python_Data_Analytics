e1 = {
    "dasis":"A825662",
    "name":"Giri Prasad P",
    "yoj":2021,
    "location":"Chennai, IN"
}

print(e1)
print(e1["name"])
print(f"{e1["name"]} is joined in the year of {e1["yoj"]}")
e1["yoj"]=2018
print(f"{e1["name"]} is joined in the year of {e1["yoj"]}")

print(f"{e1}")
e1["tech"]=['Sql','Java','React','Python']

print(f"{e1['tech']}")


e1.update({"tech":['MySQL','Microservices Java','SAP ABAP','React','Python']})

print(e1)