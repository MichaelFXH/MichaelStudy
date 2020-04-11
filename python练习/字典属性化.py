class DictObj:
    def __init__(self,d:dict):
        if isinstance(d,(dict,)):
            self.__dict__['_dict']=d
        else:
            self.__dict__['_dict']={}
    def __getattr__(self, item):
        try:
            return  self._dict[item]
        except KeyError:
            raise  AttributeError('{} not found.'.format(item))
    def __setattr__(self, key, value):
        raise NotImplemented

d={'id':100}
dod=DictObj(d)

print(dod.id)