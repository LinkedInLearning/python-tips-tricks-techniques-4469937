prefs = ['富山県', '石川県', '福井県']
capitals = ['富山市', '金沢市', '福井市']

'''
このように出力したい
富山県の県庁は富山市にあります
石川県の県庁は金沢市にあります
福井県の県庁は福井市にあります
'''

for pref, capital in zip(prefs, capitals):   
    print(f'{pref}の県庁は{capital}にあります')


prefs = ['富山県', '石川県', '福井県', '岐阜県']
capitals = ['富山市', '金沢市', '福井市']

for pref, capital in zip(prefs, capitals):   
    print(f'{pref}の県庁は{capital}にあります')

from itertools import zip_longest
for pref, capital in zip_longest(prefs, capitals, fillvalue='UnKnown'):   
    print(f'{pref}の県庁は{capital}にあります')
