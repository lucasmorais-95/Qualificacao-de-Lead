# Entradas
print('Olá, seja muito bem-vindo(a) \n'
      'Me chamo Lucas e faço parte do time Comercial da "nome da empresa" \n'
      'Será um prazer ter você com a gente! \n'
      'Farei algumas perguntas para te atender melhor\n')

graduacao = input('Vocês está cursando o ensino Medio ou Superior?: ')

if graduacao.capitalize() == 'Superior':
    # Codigo para ensino Superior
    f'{input("Qual a sua faculdade? ")}\n' \
     f'{input("Qual o seu curso? ")}\n' \
     f'{input("Está em qual período? ")}\n' \
     f'{input("Quais eventos vocês querem realizar? ")}'

elif graduacao.capitalize() == 'Medio':
    # Codigo para ensino Medio
    f"{input('Qual a sua escola? ')}\n" \
     f"{input('Em que ano você se forma? ')}" \
     f"{input('Quais eventos vocês querem realizar? ')}"

else:
    print('Desculpe, trabalhamos apenas com eventos relacioanados a jornada do estudante!'
          'Obrigado pelo contato')

comissao = input('Vocês possuem uma Comissão de Formatura Formada?(Responda "N" para Não e "S" para Sim) ')

if comissao.capitalize() == 'N':
    print('Irei te enviar várias dicas de como formar a Comissão da turma.... ')

elif comissao.capitalize() == 'S':
    print('O nosso próximo passo é marcar o nosso primeiro ....')

else:
    print('Opção invalida. Tente novamente, por favor!')
