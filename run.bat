@echo OFF
ECHO Compiling...
javac SimuladorRFID.java
ECHO Running simulator...
java SimuladorRFID schoute
java SimuladorRFID lowerbound
java SimuladorRFID chen
ECHO Generating charts...
python generatechart.py

