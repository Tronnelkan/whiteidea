import datetime
from array import array

import monobank

mono = monobank.Client(token='uREsWIdblLfSPuPtoTpT3HXvuwtEI0In464xKkH-E4nI')
info_for_client = mono.get_client_info()
client_statements = mono.get_statements('uKMWYopmu0DVxgK1oDqhIA', datetime.datetime(2021, 7, 17, 14), datetime.datetime.now())
# print(info_for_client)
# print('h' * 100)
test = 'https://send.monobank.ua/ZYiX9yTmo?amount=120.00&text=kotdasasd'
for item in client_statements:
    comment = dict(item).get('comment')
    amount = dict(item).get('amount')
    amount = amount/100
    balance = dict(item).get('balance')
    balance = balance/100
    description = dict(item).get('description')
    print(f'1.Сума платежа:{amount}\n'
          f'2.Баланс после платежа:{balance}\n'
          f'3.Описания платежа:{description}\n'
          f'4.Коментарий к платежу:{comment}')



# {'clientId': 'ZYiX9yTmo', 'name': 'Ушаков Олександр', 'webHookUrl': '', 'permissions': 'psf', 'accounts': [{'id': 'uKMWYopmu0DVxgK1oDqhIA', 'currencyCode': 980, 'cashbackType': 'UAH', 'balance': 16, 'creditLimit': 0, 'maskedPan': ['537541******8500'], 'type': 'black', 'iban': 'UA363220010000026208315232478'}, {'id': '-l1zBgBSMjYHlSpnWoz7zA', 'currencyCode': 840, 'cashbackType': 'UAH', 'balance': 0, 'creditLimit': 0, 'maskedPan': ['537541******7332'], 'type': 'black', 'iban': 'UA633220010000026205315865213'}]}
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# var = [{'id': 'bcum1ejH1vUr_04p', 'time': 1626616333, 'description': 'Часткове зняття банки «Просто так»', 'mcc': 4829,
#         'originalMcc': 4829, 'amount': 15, 'operationAmount': 15, 'currencyCode': 980, 'commissionRate': 0,
#         'cashbackAmount': 0, 'balance': 16, 'hold': True},
#        {'id': 'PSqxHovkRAHsScGV', 'time': 1626600593, 'description': 'Юрчанський', 'mcc': 4829, 'originalMcc': 4829,
#         'amount': -20000, 'operationAmount': -20000, 'currencyCode': 980, 'commissionRate': 0, 'cashbackAmount': 0,
#         'balance': 1, 'hold': True, 'receiptId': 'M4T8-M040-8148-P7BH'},
#        {'id': '465jwAmqsRDJrUc2', 'time': 1626600484, 'description': 'Від: Олена П.', 'mcc': 4829, 'originalMcc': 4829,
#         'amount': 20000, 'operationAmount': 20000, 'currencyCode': 980, 'commissionRate': 0, 'cashbackAmount': 0,
#         'balance': 20001, 'hold': True},
#        {'id': 'BoBRdOmMpH8LZrT6', 'time': 1626598482, 'description': 'Yezhachok', 'mcc': 5499, 'originalMcc': 5499,
#         'amount': -2000, 'operationAmount': -2000, 'currencyCode': 980, 'commissionRate': 0, 'cashbackAmount': 40,
#         'balance': 1, 'hold': True, 'receiptId': '77BB-T545-HAHC-XPK9'},
#        {'id': 'o3jMtoQuHYt7YthB', 'time': 1626579495, 'description': 'MOBILE BANKING', 'mcc': 6536, 'originalMcc': 6536,
#         'amount': 2000, 'operationAmount': 2000, 'currencyCode': 980, 'commissionRate': 0, 'cashbackAmount': 0,
#         'balance': 2001, 'hold': False},
#        {'id': '9jMCFpqHzOzQhi8X', 'time': 1626554993, 'description': 'Олена П.', 'comment': ':))))))))))))))))',
#         'mcc': 4829, 'originalMcc': 4829, 'amount': -20, 'operationAmount': -20, 'currencyCode': 980,
#         'commissionRate': 0, 'cashbackAmount': 0, 'balance': 1, 'hold': True, 'receiptId': 'KBKH-E1KX-25E5-B0KK'},
#        {'id': 'aWXV9VN8ma-Yevjw', 'time': 1626547743, 'description': 'Від: Олена П.', 'mcc': 4829, 'originalMcc': 4829,
#         'amount': 20, 'operationAmount': 20, 'currencyCode': 980, 'commissionRate': 0, 'cashbackAmount': 0,
#         'balance': 21, 'hold': True},
#        {'id': 'WU726Xe2WSLi-BWg', 'time': 1626540217, 'description': 'Назар К.', 'mcc': 4829, 'originalMcc': 4829,
#         'amount': -5000, 'operationAmount': -5000, 'currencyCode': 980, 'commissionRate': 0, 'cashbackAmount': 0,
#         'balance': 1, 'hold': True, 'receiptId': 'CT0E-11XB-MBEB-X22H'},
#        {'id': 'RQm1WRkaVKQlpn3y', 'time': 1626522661, 'description': 'Від: Валентин Д.', 'mcc': 4829,
#         'originalMcc': 4829, 'amount': 5000, 'operationAmount': 5000, 'currencyCode': 980, 'commissionRate': 0,
#         'cashbackAmount': 0, 'balance': 5001, 'hold': True},
#        {'id': 'k8S_QiKMBIef5F3m', 'time': 1626515238, 'description': 'Yezhachok', 'mcc': 5499, 'originalMcc': 5499,
#         'amount': -2000, 'operationAmount': -2000, 'currencyCode': 980, 'commissionRate': 0, 'cashbackAmount': 40,
#         'balance': 1, 'hold': True, 'receiptId': '3XMK-M4HP-C50X-27E7'},
#        {'id': 'Xp6dpI5HamackfgN', 'time': 1626512555, 'description': 'MOBILE BANKING', 'mcc': 6536, 'originalMcc': 6536,
#         'amount': 2000, 'operationAmount': 2000, 'currencyCode': 980, 'commissionRate': 0, 'cashbackAmount': 0,
#         'balance': 2001, 'hold': False}]`

