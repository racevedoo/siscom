#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def plot(medida,titulo,nome):
	fig = plt.figure()
	ax = fig.add_subplot(1,1,1,axisbg='white')
	plt.plot(tags_all,medida)
	plt.title(titulo)
	plt.ylabel('Slots')
	plt.xlabel('Etiquetas')
	plt.savefig(nome+'.png')
tags_all = [100,200,300,400,500,600,700,800,900,1000]
media_totais = []
media_vazios = []
media_colisao = []
for tags in tags_all:
	totais,vazios,colisao = np.loadtxt('schoute'+str(tags)+'.csv',delimiter=',',unpack=True)
	media_totais.append(np.mean(totais))
	media_vazios.append(np.mean(vazios))
	media_colisao.append(np.mean(colisao))

plot(media_totais, 'Slots totais', 'totais')
plot(media_colisao, 'Slots em colisao', 'colisao')
plot(media_vazios, 'Slots vazios', 'vazios')