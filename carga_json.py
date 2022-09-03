objeto_json=[
    {
        "nombre":"ulises",
        "apellido":"juarez"
    },
    {
        "nombre":"mariela",
        "apellido":"hernandez"
    }
]


for i in objeto_json:
    print(i["nombre"])
    print(i["apellido"])
    print("************************************")


print(type(objeto_json))