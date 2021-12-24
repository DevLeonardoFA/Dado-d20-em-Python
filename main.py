# this is a API for return a d20 result
# coding: utf-8
import random
import codecs
from flask import Flask

app = Flask(__name__)

# começo da brincadeira
class dado:
  def __init__(self):
    self.valor_min = 0
    self.frase = "Qual dado quer jogar?\n\n[0] - d2 \n[1] - d4 \n[2] - d6 \n[3] - d8 \n[4] - d10 \n[5] - d20 \n\nescolha: "
    self.jogadas = 1

  def Iniciar(self):

    while self.jogadas == 1 :
      
      resposta = input(self.frase)

      if(resposta == '0' ):
        self.Valor(2)
      else:
        if(resposta == '1' ):
          self.Valor(4)
        else:
          if(resposta == '2' ):
            self.Valor(6)
          else:
            if(resposta == '3' ):
              self.Valor(8)
            else:
              if(resposta == '4' ):
                self.Valor(10)
              else:
                if(resposta == '5' ):
                  self.Valor(20)
                else:
                  print('erro');


  def Valor(self, max):
    resultado = random.randint(self.valor_min, max)
    print('\nresultado do dado: ', resultado, '\n\n')

    jogar_novamente = input('quer jogar novamente? [s] [n] \n\nresposta: ')
    print('\n')
    if(jogar_novamente == 'sim' or jogar_novamente == 's'):
      self.jogadas = 1;
    else:
      self.jogadas = 0;


dado = dado()
dado.Iniciar()

# abrindo um outro arquivo
# home = codecs.open("test.html", 'r')

# # criando rota
# @app.route('/')
# def front():
#   return home.read()
    
# # executando servidor
# app.run(host='0.0.0.0')