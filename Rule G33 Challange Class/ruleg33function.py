"""Rule G33 Funcations"""

def calc_accuredinterest(num):
    """calc_accuredinterest"""
    to_dec = float(trunc_string(num, 3))
    return '%.2f'%(to_dec)

def calc_dollarprice(num):
    """calc_dollarprice"""
    return float(trunc_string(num, 3))

def calc_yield(num):
    """calc_yield"""
    to_dec = float(trunc_string(num, 4))
    return '%.3f'%(to_dec)

def trunc_string(num, idx):
    """truncate_string"""
    to_str = str(num)
    split_str1, split_str2 = to_str.split(".")
    truncate_str = split_str2[0:0+idx]
    result_str = split_str1 + "." + truncate_str
    return result_str
