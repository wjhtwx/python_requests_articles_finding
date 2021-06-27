class unexpected_json_data(Exception):
    def __init__(self, msg):
        self.msg=msg
    def __str__(self):
        print(self.msg)