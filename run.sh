javac Simulador.java
if [ $? -ne 0 ]; then
	echo "Compile failed"
	exit 1
fi
java Simulador $1
if [ $? -ne 0 ]; then
	echo "Simulator failed"
	exit 2
fi
python generatechart.py $1
