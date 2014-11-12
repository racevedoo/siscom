#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def plot(medida,titulo,nome):
	fig = plt.figure()
	ax1 = fig.add_subplot(1,1,1,axisbg='white')
	plt.plot(tags_all,medida)
	plt.title(titulo)
	plt.ylabel('Slots')
	plt.xlabel('Etiquetas')
	plt.savefig(nome+'.png')
tags_all = [100,200,300,400,500,600,700,800,900,1000]
cnt = 0
media_totais = []
media_vazios = []
media_colisao = []
dp_totais = []
dp_vazios = []
dp_colisao = []
for tags in tags_all:
	totais,vazios,colisao = np.loadtxt('schoute'+str(tags)+'.csv',delimiter=',',unpack=True)
	media_totais.append(np.mean(totais))
	media_vazios.append(np.mean(vazios))
	media_colisao.append(np.mean(colisao))
	dp_totais.append(np.std(totais))
	dp_vazios.append(np.std(vazios))
	dp_colisao.append(np.std(colisao))
	cnt = cnt + 1

plot(media_totais, 'Slots totais', 'totais')
plot(media_colisao, 'Slots em colisao', 'colisao')
plot(media_vazios, 'Slots vazios', 'vazios')