'''
Closure e funções que retornam outras funções 
'''

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar
    

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

# print(falar_boa_noite("ana")) #closure é fechar a função esse () "é" do return saudar
# print(falar_bom_dia('Ana')) 

for nome in ['A', 'B', 'C']:
    print(falar_bom_dia(nome))