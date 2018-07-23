import json

# author 'Lucian'

class StudentJson(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score


def student2json(std):
    return{
        'name':std.name,
        'age':std.age,
        'score':std.score
    }

s = StudentJson('Bob',18,90)


d = json.dumps(s,default=student2json)

print('d:',d)
m = json.loads(d)
print('m:',m)
