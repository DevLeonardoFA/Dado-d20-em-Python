# this is a API for return a d20 result
# coding: utf-8
import random

class d20:
  def __init__(self):
    self.valor_min = 0
    self.valor_max = 20
    self.frase = "quer jogar o d20?\n"

  def Iniciar(self):
    resposta = input(self.frase)
    if(resposta == 'sim' or resposta == 's'):
      self.Valor()
    else:
      print('thks')
      
  def Valor(self):
    print(random.randint(self.valor_min, self.valor_max))

dado = d20()
dado.Iniciar()