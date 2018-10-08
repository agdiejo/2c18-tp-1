import time, math
from flask import Flask
app = Flask(__name__)

@app.route("/veloz")
def root():
    return "Hola desde veloz py"

@app.route("/timeout")
def timeout():
    time.sleep(10)
    return "Hola desde timeout py"

@app.route("/intensivo")
def intensivo():
	total = 100000
	for i in range(total):
		math.sqrt(i)

	return "listo, procesado " + str(total) + " raices en py" 

if __name__=="__main__":
    app.run()