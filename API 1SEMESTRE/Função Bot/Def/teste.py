#funcionando com dados ficticios

lista_clientes = [
{"cliente":"Julia", "tem_gravação":"True", "tem_foto":"False"},
{"cliente":"Julia", "tem_gravação":"True", "tem_foto":"True"}
]

def filtro_cliente(planilha, provag, provaf):
    for nome in planilha:
        if nome.get(provag) == "False" or nome.get(provaf) == "False":
            return print(nome)
    return None

resultado = filtro_cliente(lista_clientes,"tem_gravação", "tem_foto")
print(resultado)