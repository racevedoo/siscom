javac SimuladorRFID.java
if [ $? -ne 0 ]; then
	echo "Compile failed"
	exit 1
fi
java SimuladorRFID $1
if [ $? -ne 0 ]; then
	echo "Simulator failed"
	exit 2
fi
python generatechart.py $1
