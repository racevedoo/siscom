#!/bin/bash
methods=("lowerbound" "schoute" "chen")
javac SimuladorRFID.java
if [ $? -ne 0 ]; then
	echo "Compile failed"
	exit 1
fi
for method in "${methods[@]}"
do
	:
	echo "Executing $method ..."
	java SimuladorRFID $method
	if [ $? -ne 0 ]; then
		echo "Simulator failed"
		exit 2
	fi
done 

python generatechart.py
eog totais.png
eog vazios.png
eog colisao.png