"""Rule G33 Funcations"""

def calc_accuredinterest(num):
    """calc_accuredinterest"""
    to_str = str(num)
    split_str1, split_str2 = to_str.split(".")
    truncate_str = split_str2[0:0+3]
    result_str = split_str1 + "." + truncate_str
    to_dec = float(result_str)
    result = '%.2f'%(to_dec)
    print "Accured Interest: ", result
    return

def calc_dollarprice(num):
    """calc_dollarprice"""
    to_str = str(num)
    split_str1, split_str2 = to_str.split(".")
    truncate_str = split_str2[0:0+3]
    result_str = split_str1 + "." + truncate_str
    to_dec = float(result_str)
    print "Dollar Price: ", to_dec
    return

def calc_yield(num):
    """calc_yield"""
    to_str = str(num)
    split_str1, split_str2 = to_str.split(".")
    truncate_str = split_str2[0:0+4]
    result_str = split_str1 + "." + truncate_str
    to_dec = float(result_str)
    result = '%.3f'%(to_dec)
    print "Yield: ", result
    return
