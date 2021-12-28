
Ad_Name = []
Ad_Value = []

def Tr():
    while True:
        find(input('Insert Keyword >> '))

def find(e):
    if e == 'Create Keyword':
        f = input('Name >> ')
        s = input('Keyword >> ')
        Ad_Name.append(f)
        Ad_Value.append(s)
        return True
    else:
        print(Ad_Name[Ad_Value.index(e)])

if __name__ == '__main__':
    Tr()