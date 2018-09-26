import time
from flask import Flask
app = Flask(__name__)

@app.route("/veloz")
def root():
    return "Hola desde veloz py"

@app.route("/timeout")
def timeout():
    time.sleep(10)
    return "Hola desde timeout py"

if __name__=="__main__":
    app.run()