produto = {
    'nome' : 'caneta azul',
    'preco' : 2.5,
    'categoria' : 'escritorio',

}

dc = {
    chave: valor.upper()
    if isinstance(valor,str) else valor
    for chave , valor 
    in produto.items()
}

print(dc)