from structure.database import ImitateDatebase

db = ImitateDatebase()

class WriteData:
    def __init__(self, **dict_):
        self.dict_ = dict_

    def execute(self):
        return db.write(self.dict_)
    
class ReadData:
    
    def execute(self):
        dbm = db.read()
        return dbm
    

if __name__ == '__main__':
    read = ReadData()
    file = read.execute()
    print(file['Patrich'])