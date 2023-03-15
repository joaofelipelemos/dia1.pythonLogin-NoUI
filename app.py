'''
Deve permitir cadastrar novo usuário;
    5 Qs: 
        1. Quais dados necessários?
            Usuário e Senha.
        2. Oque devo fazer com estes dados?
            Registrar usuário e senha informado.
        3. Quais as restrições?
            Não permitir usuários duplicados.
        4. Qual o resultado esperado?
            Novo usuário e senha cadastrado.
        5. Qual a sequencia de passos para chegar ao resultado esperado?
            Receber usuário;
            Receber senha;
            Verificar duplicidade;
            Se único, segue a gravação;
Não permitir usuário duplicado;
Permitir que usuários cadastrados façam login;
Alertar caso login ou senha errado;
'''

# Pergunta se quer fazer login ou cadastrar
user_escolha = input(
    '1. Deseja cadastrar novo usuário? 2. Deseja realizar login?')
# Armazenando usuários existentes
usuarios = ['Pedro', 'João', 'José']
senhas = ['123', '456', '789']
# Código cadastro
match user_escolha:
    case '1':
        # Recebendo novo usuário
        usuario_input = input('Qual o usuário para cadastro? ')
        if usuario_input in usuarios:
            print('Usuário existente')
        else:
            # Recebendo nova senha
            senha_input = input('Digite uma senha para registrar: ')
    # Verifica duplicidade
            print('Usuário Cadastrado')
            usuarios.append(usuario_input)
            senhas.append(senha_input)
    # Código para login
    case '2':
        # Recebendo login usuário
        usuario_login = input('Digite seu login: ')
        # Recebendo nova senha
        senha_login = input('Digite sua senha: ')
        # Verifica na lista se usuário existe
        sucesso = False
        for indice, usuario in enumerate(usuarios):
            if usuario_login == usuario and senha_login == senhas[indice]:
                print('Login realizado')
                sucesso = True
            elif sucesso == False:
                print('Usuário ou senha inválido')
    case _:
        print('Digite apenas 1 ou 2')
