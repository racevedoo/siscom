#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import sys

def plot(medida,titulo,nome):
	fig = plt.figure()
	ax = fig.add_subplot(1,1,1,axisbg='white')
	plt.plot(tags_all,medida[0],label='Chen')
	plt.plot(tags_all,medida[1],label='Schoute')
	plt.plot(tags_all,medida[2],label='Lower-Bound')
	plt.title(titulo)
	plt.legend(loc='upper left')
	plt.ylabel(titulo)
	plt.xlabel('Etiquetas')
	plt.savefig(nome+'.png')
names = ['chen','schoute','lowerbound']
tags_all = [100,200,300,400,500,600,700,800,900,1000]
media_totais = [[],[],[]]
media_vazios = [[],[],[]]
media_colisao = [[],[],[]]
for i in range(0,len(names)):
	name = names[i]
	for tags in tags_all:
		totais,vazios,colisao = np.loadtxt(name+str(tags)+'.csv',delimiter=',',unpack=True)
		media_totais[i].append(np.mean(totais))
		media_vazios[i].append(np.mean(vazios))
		media_colisao[i].append(np.mean(colisao))

plot(media_totais, 'Total de slots', 'totais')
plot(media_colisao, 'Slots em colisao', 'colisao')
plot(media_vazios, 'Slots vazios', 'vazios')