"""Rule G33 Funcations"""

def calc_accuredinterest(num):
    """calc_accuredinterest"""
    to_dec = float(truncate_num(num, 3))
    return '%.2f'%(to_dec)

def calc_dollarprice(num):
    """calc_dollarprice"""
    return float(truncate_num(num, 3))

def calc_yield(num):
    """calc_yield"""
    to_dec = float(truncate_num(num, 4))
    return '%.3f'%(to_dec)

def truncate_num(num, idx):
    """truncate_string"""
    to_str = str(num)
    split_str1, split_str2 = to_str.split(".")
    return split_str1 + "." +  split_str2[0:0+idx]
