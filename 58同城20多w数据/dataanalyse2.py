import pymongo
import charts

client = pymongo.MongoClient('localhost',27017)
ceshi = client['copy']
item_info = ceshi['item_info']

'''for i in item_info.find():             #������ϴ
    if '�ּ�' in i['price']:
        item_info.update_one({'_id':i['_id']},{'$set':{'price':i['price'].split('��')[1].split('Ԫ')[0]}})
    else:
        if 'Ԫ' in i['price']:
            item_info.update_one({'_id':i['_id']},{'$set':{'price':i['price'].split(' ')[0]}})
        else:
            pass
'''

calc = 0
calc2 = 0
calc3 = 0
for i in item_info.find():
    if '����' not in i['price']:
        if '��' not in i['price']:
            if int(i['price']) > 2500 and int(i['price']) < 3000:
                calc += 1
        else:
            calc2 += 1
print(calc, calc2)

def gen_data():
    calc = 0
    for i in item_info.find():
    if '����' not in i['price']:
        if '��' not in i['price']:
            if int(i['price']) < 100:
                calc += 1
            if int(i['price']) > 2500 and int(i['price']) < 3000:
                calc += 1