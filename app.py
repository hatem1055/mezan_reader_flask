from flask import Flask,render_template,request,redirect,url_for
from flask_cors import CORS, cross_origin
import time
from read_config import Config
from read_mezan import SerialReader,SerialConnectionError,SerialReadException
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/get_qty',)
@cross_origin()
def get_qty():
    config = Config() 

    try:

        serial_reader = SerialReader(config.com_port)
        qty = serial_reader.get_actual_data()
        return {
            "qty" : qty
        }
    except SerialConnectionError as e:
        return {
            "error" : f"Serial Port Connection Error {e.message}"
        }
    except SerialReadException as e:
        return {
            "error" : f"Serial Port Read Error {e.message}"
        }

if __name__ == '__main__':
    config = Config() 
    app.run(debug=True,port=config.port)
