#!/usr/bin/env python
# encoding: utf-8
import random
import math

# Classe para gera��o de n�meros aleat�rios segundos v�rias distribui��es
# Apenas a distribui��o exponencial negativa est� definida


def exponencial(media):
	# """Gera um n�mero segundo uma distribui��o exponencial negativa de m�dia m"""
	return (-media*math.log(random.random()))

def normal(dist):
	 return random.gauss(dist[0], dist[1])

#print Aleatorio().exponencial(2) #test
