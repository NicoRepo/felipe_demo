import enum
import itertools
import json
from math import factorial
from operator import indexOf
from random import sample
from itertools import combinations
from typing import Iterable
PERROS = [['perro-0',  3], ['perro-1', 4], ['perro-2', 5], ['perro-3', 6], ['perro-4', 7], ['perro-5', 8], ['perro-6', 9], ['perro-7', 1]]
PISTOLAS = [['pistola-0', 5], ['pistola-1', 6], ['pistola-2', 8], ['pistola-3', 4], ['pistola-4', 10], ['pistola-5', 19], ['pistola-6', 3]]
GATOS = [['gato-0', 1], ['gato-1',  2], ['gato-2', 3], ['gato-3', 4], ['gato-4', 5],  ['gato-5', 6], ['gato-6', 7], ['gato-7', 8], ['gato-8', 9]]
keys = {}

CONJUNTOS = [{"list": PERROS, "sample": 5}, {"list": PISTOLAS, "sample": 3}, {"list": GATOS, "sample": 5}]

def main():
  print(total_iterations(CONJUNTOS))
  glob = 0
  while glob <= total_iterations(CONJUNTOS):
    index = ""
    tmp = []
    for i, elem in enumerate(CONJUNTOS):  
      _sample = sample(elem.get('list'), elem.get('sample'))
      for s_item in _sample:
        tmp.append(s_item[1])
        for i, _elem in enumerate(elem.get('list')):
          if s_item[0] == _elem[0]:
            index+=str(i)
    if not keys.get(index):
      print(f"{index} generated")
      glob+=1  
      keys.update({index: sum(tmp)})
    else:
      print('Ya Generado')
    #print(glob)
  print(len(keys))
  #print(json.dumps(keys, indent=4))
  #print(sum(tmp))

def combinatory(conjunto: list, elementos: int) -> Iterable:
  return combinations(conjunto, elementos)

def total_iterations(conjuntos: list):
  a = []
  for c in conjuntos:
    a.append(combinatory(c.get('list'), c.get("sample")))
  r = 1
  for res in a:
    r*=len(list(res))
  return r

if __name__ == "__main__":
  
  main()
  
  
  
  
  