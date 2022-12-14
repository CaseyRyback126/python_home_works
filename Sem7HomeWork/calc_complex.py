def calc_comp(real, real1, oper):
    if oper == '+':
        res = complex(real.replace(' ', '')) + complex(real1.replace(' ', ''))
    elif oper == '-':
        res = complex(real.replace(' ', '')) - complex(real1.replace(' ', ''))
    elif oper == '*':
        res = complex(real.replace(' ', '')) * complex(real1.replace(' ', ''))
    else:
        res = complex(real.replace(' ', '')) / complex(real1.replace(' ', ''))
    return res


print(calc_comp('4+5j', '1+2j', '+'))
