from Model import XmlRecordRepository

class Controller:
    def __init__(self,path):
        self.model=XmlRecordRepository(path)
    
    def get_record_list(self):
        record_list=[]
        for record in self.model.get_all():
            record_list.append(record.to_list())
        return record_list    

    def remove_elm(self,key:str):
        self.model.remove_record(key)
    
    def save(self):
        self.model.__save()
    

