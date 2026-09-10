class Store:
    def __init__(self):self.results={}
    def run(self,key,fn):
        if key in self.results:return self.results[key],True
        self.results[key]=fn()
        return self.results[key],False
