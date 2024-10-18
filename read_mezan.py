from serial import Serial,PARITY_NONE,STOPBITS_ONE,EIGHTBITS
import time 

class SerialReadException(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(self.message)
class SerialConnectionError(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(self.message)
class SerialReader:
    ser = None
    def __init__(self,port):
        try:
            self.ser = Serial(
                port=port,\
                baudrate=9600,\
                parity=PARITY_NONE,\
                stopbits=STOPBITS_ONE,\
                bytesize=EIGHTBITS,\
                    timeout=0)
        except:
            raise SerialConnectionError("Connection Failed")
    def get_raw_data(self):
        while True:
            serialString = self.ser.readline()
            # Print the contents of the serial data
            ascii_serialString = serialString.decode("Ascii")
            if len(ascii_serialString) > 0:
                try:
                    return ascii_serialString
                except:
                    raise SerialReadException("Read Cannot Be Turned To Ascii")

    def _get_actual_data(self):
        raw_data = self.get_raw_data()
        if raw_data == "":
            raise SerialReadException("Empty Read")
        if len(raw_data.split(" ")) < 3:
            raise SerialReadException(f"Invalid Data Format {raw_data}")
        number = None
        raw_data_split = raw_data.split(" ")
        for data_point in raw_data_split:
            try:
                number = float(data_point)
                break
            except:
                continue
        if number is  None:
            raise SerialReadException(f"Invalid Data Format {raw_data}")
        try:
            return float(number)
        except:
            raise SerialReadException(f"Invalid Data Format {raw_data}")
    def get_actual_data(self,counter = 0):
        try:
            return self._get_actual_data()
        except Exception as e:
            if counter == 100:
                raise e
            time.sleep(0.1)
            return self.get_actual_data(counter+1)
