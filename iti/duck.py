

def cal_money(minute=1):
    if isinstance(minute, float) or isinstance(minute, int):
        return minute * 10
    else:
        print("--- minute must be int ")