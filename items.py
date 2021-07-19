from dataclasses import dataclass
from unicodedata import category


@dataclass
class Item:
    id: int
    category: str
    title: str
    description: str
    price: int


item1i = Item(id=1, category='i', title='Названия 1', description='Описания 1', price=20)
item2i = Item(id=2, category='i', title='Названия 1', description='Описания 1', price=121)
item3i = Item(id=3, category='i',title='Названия 1', description='Описания 1', price=122)
item4i = Item(id=4, category='i', title='Названия 1', description='Описания 1', price=123)
item5i = Item(id=5, category='i', title='Названия 1', description='Описания 1', price=124)
item6i = Item(id=6, category='i', title='Названия 1', description='Описания 1', price=125)
item7y = Item(id=7, category='y', title='Названия 1', description='Описания 1', price=1)
item8y = Item(id=8, category='y', title='Названия 1', description='Описания 1', price=1)
item9y = Item(id=9, category='y', title='Названия 1', description='Описания 1', price=1)
item10y = Item(id=10, category='y', title='Названия 1', description='Описания 1', price=1)
item11y = Item(id=11, category='y', title='Названия 1', description='Описания 1', price=1)
item12y = Item(id=12, category='y', title='Названия 1', description='Описания 1', price=1)
item13s = Item(id=13, category='s', title='Названия 1', description='Описания 1', price=1)
item14s = Item(id=14, category='s', title='Названия 1', description='Описания 1', price=1)
item15s = Item(id=15, category='s', title='Названия 1', description='Описания 1', price=1)
item16s = Item(id=16, category='s', title='Названия 1', description='Описания 1', price=1)
item17s = Item(id=17, category='s', title='Названия 1', description='Описания 1', price=1)
item18s = Item(id=18, category='s', title='Названия 1', description='Описания 1', price=1)
item19f = Item(id=19, category='f', title='Названия 1', description='Описания 1', price=1)
item20f = Item(id=20, category='f', title='Названия 1', description='Описания 1', price=1)
item21f = Item(id=21, category='f', title='Названия 1', description='Описания 1', price=1)
item22f = Item(id=22, category='f', title='Названия 1', description='Описания 1', price=1)
item23f = Item(id=23, category='f', title='Названия 1', description='Описания 1', price=1)
item24f = Item(id=24, category='f', title='Названия 1', description='Описания 1', price=1)
item25t = Item(id=25, category='t', title='Названия 1', description='Описания 1', price=1)
item26t = Item(id=26, category='t', title='Названия 1', description='Описания 1', price=1)
item27t = Item(id=27, category='t', title='Названия 1', description='Описания 1', price=1)
item28t = Item(id=28, category='t', title='Названия 1', description='Описания 1', price=1)
item29t = Item(id=29, category='t', title='Названия 1', description='Описания 1', price=1)
item30t = Item(id=30, category='t', title='Названия 1', description='Описания 1', price=1)
item31tt = Item(id=31, category='tt', title='Названия 1', description='Описания 1', price=1)
item32tt = Item(id=32, category='tt', title='Названия 1', description='Описания 1', price=1)
item33tt = Item(id=33, category='tt', title='Названия 1', description='Описания 1', price=1)
item34tt = Item(id=34, category='tt', title='Названия 1', description='Описания 1', price=1)
item35tt = Item(id=35, category='tt', title='Названия 1', description='Описания 1', price=1)
item36tt = Item(id=36, category='tt', title='Названия 1', description='Описания 1', price=1)
item37v = Item(id=37, category='v', title='Названия 1', description='Описания 1', price=1)
item38v = Item(id=38, category='v', title='Названия 1', description='Описания 1', price=1)
item39v = Item(id=39, category='v', title='Названия 1', description='Описания 1', price=1)
item40v = Item(id=40, category='v', title='Названия 1', description='Описания 1', price=1)
item41v = Item(id=40, category='v', title='Названия 1', description='Описания 1', price=1)
item42v = Item(id=40, category='v', title='Названия 1', description='Описания 1', price=1)

items_instagram = [item1i, item2i, item3i, item4i, item5i, item6i]
items_youtube = [item7y, item8y, item9y, item10y, item11y, item12y]
items_selling = [item13s, item14s, item15s, item16s, item17s, item18s]
items_facebook = [item19f, item20f, item21f, item22f, item23f, item24f]
items_telegram = [item1i, item2i, item3i, item4i, item5i, item6i]
items_tiktok = [item1i, item2i, item3i, item4i, item5i, item6i]
items_otviti = [item1i, item2i, item3i, item4i, item5i, item6i]
