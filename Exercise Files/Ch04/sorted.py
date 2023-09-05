prefs = ('Toyama', 'Ishikawa', 'Fukui','Gifu')
populations = (1_066_328,1_154_008,786_740,2_031_903)

print(sorted(prefs))
print(sorted(populations))

print(sorted(zip(prefs,populations)))
print(sorted(zip(prefs,populations),key=lambda x: x[1]))    #ラムダ式でキーを指定
print(sorted(zip(prefs,populations),key=lambda x: -x[1]))   #マイナス指定で降順に
print(sorted(zip(prefs,populations),key=lambda x: x[0]))