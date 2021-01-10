def sum_arguments(max_value,args):
    suma=0
    for elem in args:
        if isinstance(max_value,int):
            if isinstance(elem,int) and elem<=max_value:
                suma +=elem
        else:
            if isinstance(elem,int):
                suma +=elem
    return suma

def capital_case(x):
    if not isinstance(x,str):
        raise TypeError ('Prosze wprowadz napis')
    return x.capitalize()