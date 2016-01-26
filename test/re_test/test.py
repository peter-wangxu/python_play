class InterfaceMeta(type):
    def __new__(cls, name, parents, dct):
        # carete a class_id if ti's not specified
        print "cls:", cls
        if 'zzz_sss' not in dct:
            dct['zzz_sss'] = name.lower()
        
        if 'file' in dct:
            filename = dct['file']
            dct['file'] = open(filename, 'w')
        print dct
        return super(InterfaceMeta, cls).__new__(cls, name, parents, dct)


Interface = InterfaceMeta("Interface", (), dict(file='temp.txt'))
print(Interface.zzz_sss)
print(Interface.file)