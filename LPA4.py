# QUESTÃO 3 DE 4 (AULA 5)


#Início da função metragem_limpeza()
def metragem_limpeza():    
  print('-------------------- Menu 1 de 3 - Metragem Limpeza---------------')
  while True:
    try: #tentativa de execução do código e caso não consiga executar por conta de um erro algum erros, vai retornar o que tem dentro do except.
      metragem = float(input('Entre com a metragem da casa (m²): '))
      if 30 <= metragem < 300:                
        print ('Será necessário um funcionário para a limpeza ')
        return 60 + 0.3 * metragem #Saída da função para o programa principal.            
      elif 300 <= metragem < 700:   
        print ('Serão necessários(as) dois(duas) funcionário(as) para a limpeza ')             
        return 120 + 0.5 * metragem                
      else:
        print('!! Não aceitamos casas com metragem menor que 30m² ou maior que 700m²!!')
    except  ValueError: #Caso usuário digite letras ou outro caractere não permitido.
      print('Digite apenas caracteres válidos.')
#Fim da função metragem_limpeza()




#Início da função tipo_limpeza()
def tipo_limpeza():
  print ('*********************************************************************')
  print('-------------------- Menu 2 de 3 - Tipo Limpeza-----------------------')
  while True:
    tipo_da_limpeza = input('Entre com o tipo de Limpeza: \n' +
                            'B – Básica - Indicada para sujeiras semanais ou quinzenais \n' +
                            'C – Completa - Indicada para sujeiras antigas e/ou não rotineira \n'  )
    tipo_da_limpeza = tipo_da_limpeza.upper()
    if tipo_da_limpeza == 'B':
      print('Você selecionou a limpeza BÁSICA')
      return 1.00
    elif tipo_da_limpeza == 'C':
      print('Você selecionou a limpeza COMPLETA')
      return 1.30
    else:
        print('!!!!! Opção Inválida !!!!')        
        continue #Se cair nessa opcão, volta para o início do laço/pergunta.
    
#Fim da função tipo_limpeza()




#Início da função adicional_limpeza()
def adicional_limpeza():
  print ('**************************************************************************')
  print('-------------------- Menu 3 de 3 - Adicional Limpeza-----------------------')
  acumulador = 0 #Necessário valor inicial na variável
  while True:
    adicional = input('Deseja mais algum adicional:? \n' +
                      '0- Não desejo mais nada (encerrar) \n' +
                      '1- Passar 10 peças de roupas - R$ 10.00 \n' +
                      '2- Limpeza de 1 Forno/Micro-ondas - R$ 12,00 \n' +
                      '3- Limpeza de 1 Geladeira/Freezer - R$ 20,00 \n' +
                      '>>')
    if adicional == '0':
      return acumulador #variável que recebe ela mesma
    elif adicional == '1':
      acumulador = acumulador + 10 #variável que recebe ela mesma mais o valor 10
      continue #volta para o início deste menu
    elif adicional == '2':
      acumulador = acumulador + 12 #variável que recebe ela mesma mais o valor 12
    elif adicional == '3':
      acumulador = acumulador + 20 #variável que recebe ela mesma mais o valor 20


#Fim da função adicional_limpeza()




#Início do Main
print('Bem vindo ao Programa de Serviços de Limpeza da Nataly Rossini')
print('***********************************************************************')
valor_metragem = metragem_limpeza() #recebe o dado de saída do return desta função
multiplicador = tipo_limpeza() #recebe o dado de saída do return desta função
adicional_da_limpeza = adicional_limpeza() #recebe o dado de saída do return desta função
total = (valor_metragem * multiplicador) + adicional_da_limpeza #equação que a empresa cobra por limpeza
print('****************************************************************************')
print('TOTAL: R$ {:.2f} (Metragem: R$ {:.2f} * tipo: R$ {:.2f} + adicional: R$ {:.2f}) ' .format(total, valor_metragem, multiplicador, adicional_da_limpeza))  #total descritivo