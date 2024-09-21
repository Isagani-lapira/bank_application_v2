
from abc import ABC
import json

class AbstractBankDao(ABC):
    
    def load_file_data(self)->dict:
        file = open(f'./data/{self.get_file_name()}')
        content = json.loads(file.read())
        
        file.close()
        return content
    
    def _insert_new_data(self,data:dict):
        current_data = self.load_file_data()
        current_data.update(data)

        new_data = json.dumps(current_data,indent=2)
        self._write_to_file(new_data)

    def _write_to_file(self,new_data:str):
        file =  open(f'./data/{self.get_file_name()}','w')
        file.write(new_data)

        
    def get_file_name(self):
        pass