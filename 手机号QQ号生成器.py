import random
# 对抗广告之手机号 QQ号生成器
def make(number):
    o0 = ['0', '零', '零','灵','玲','〇','囹','林','霖','临']
    o1 = ['1', '一', '壹','衣','伊','医','依']
    o2 = ['2', '二', '贰','尔','而','儿','弍']
    o3 = ['3', '三', '叁','删','山','杉','珊']
    o4 = ['4', '四', '肆']
    o5 = ['5', '五', '伍']
    o6 = ['6', '六', '陆']
    o7 = ['7', '七', '柒']
    o8 = ['8', '八', '捌']
    o9 = ['9', '九', '玖']
    ynumber = [o0, o1, o2, o3, o4, o5, o6, o7, o8, o9]
    numbers=str(number)
    rNum=[]
    for n in numbers:
        tn=random.choice(random.choice(ynumber[int(n)]))
        rNum.append(tn)
    return ''.join(rNum)

for i in range(100):
    print(make(809468582))
