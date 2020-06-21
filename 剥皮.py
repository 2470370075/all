l=[1,2,[2,3,[4]]]

def func(x):
    l2 = []
    def func2(x):
        for i in x:
            if isinstance(i,list):
                func2(i)
            else:
                l2.append(i)


    func2(x)
    print(l2)
func(l)
