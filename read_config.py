import json
class Config:
    port = 8001
    com_port = "COM4"
    def __init__(self):
        with open('config.json', 'r') as f:
            config_data = json.load(f)
            self.port = config_data['server_port']
            self.com_port = config_data['com_port']

