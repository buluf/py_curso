"""
input() -> Todo dado recebido via input é do tipo String

"""

# entrada de dados
# print("Qual seu nome?")
nome = input('Qual seu nome? ')

# Saída de dados

# exemplo de print 'antigo' 2.x
# print('Seja bem-vindo(a) %s' % nome)

# Exemplo de print 'moderno' 3.x
# print('Seja bem-vindo(a) {0}'.format(nome))

# Exemplo de print "mais atual" 3.7
print(f'Seja bem-vindo(a) {nome}')

# print('Qual a sua idade? ')
idade = input('Qual a sua idade? ')
# Processamento


# Saída
# Exemplo de print 'antigo' 2.x
# print('O(A) %s tem %s anos' % (nome, idade))

# Exemplo de print 'moderno' 3.x
# print('O(A) {0} tem {1} anos'.format(nome, idade))

# Exemplo de print "mais atual" 3.7
print(f'O(A) {nome} tem {idade} anos')

print(f'O {nome} nasceu em {2020 - int(idade)}')

