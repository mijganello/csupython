dict1 = { 'trunk': 'хобот', 'wasted': 'потрачено' }
dict2 = { 'nail': 'гвоздь', 'trunk': 'ствол' }



def getlist(a,b):
    a_keys = list(dict.keys(a))
    a_vals = list(dict.values(a))

    b_keys = list(dict.keys(b))
    b_vals = list(dict.values(b))

    dict_creator(a_keys, a_vals, b_keys, b_vals)


def dict_creator(ak,av,bk,bv):
    tmp_keys = []
    tmp_vals = []
    
    for x in ak:
        if x in bk:
            tmp_keys.append(x), tmp_vals.append(bv[bk.index(x)])
        else:
            tmp_keys.append(x), tmp_vals.append(av[ak.index(x)])
    
    for x in bk:
        if x not in ak:
            tmp_keys.append(x), tmp_vals.append(bv[bk.index(x)])
    
    final_dict = dict(zip(tmp_keys, tmp_vals))
    print(final_dict, type(final_dict))

getlist(dict1, dict2)
