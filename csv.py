import os,json
class CSV(object):
    def __init__(self,name=False,addition=False,to_json=False):
        if not name:
            self.name=str(len(os.listdir()))+".csv"
        else:
            self.name=name
        if addition:
            self.f=open(self.name,"a")
        else:
            self.f=open(self.name,"w")
        self.lines=0
        self.to_json=to_json
    def rows(self,data):
        t_data=[]
        for i in data:
            t_data.append(str(i))
        if self.lines==0:
            if self.to_json:
                wei=0
                self.dic={}
                self.sl={}
                for z in t_data:
                    self.dic[z]=[]
                    self.sl[wei]=z
                    wei+=1
            self.col=" ,"+",".join(t_data)+"\n"
        else:
            if self.to_json:
                el=0
                for z in data:
                    self.dic[self.sl[el]].append(z)
                    el+=1
            self.col=str(self.lines)+","+",".join(t_data)+"\n"
        self.f.write(self.col)
        self.lines+=1
    def cols(self,col_data):
        if self.lines==0:
            self.rows(col_data)
        else:
            print("The first row is already in,please user add_data()")
    def add_data(self,data):
        self.rows(data)
        return self.lines
    def close(self):
        self.f.close()
