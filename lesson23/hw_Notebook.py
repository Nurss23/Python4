class Notebook:
    def __init__(self,ram,memory,cpu):
        self.ram = int(ram)
        self.memory = int(memory)
        self.cpu = int(cpu)

    def info(self):
        return dct
    
    def add_notebook(self,dct):
        res = ([("ram", self.ram), ("memory", self.memory), ("cpu", self.cpu)])
        dct.update(res)

notebook = Notebook(12,500,4)
dct = {}
notebook.add_notebook(dct)
print(notebook.info())