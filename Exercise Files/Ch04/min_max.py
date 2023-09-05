prefs = ['Toyama', 'Ishikawa', 'Fukui','Gifu']
populations = [1_066_328,1_154_008,786_740,2_031_903]
print(min(prefs))
print(max(prefs))
print(min(populations))
print(max(populations))

print(min(zip(prefs,populations)))
print(max(zip(prefs,populations)))

print(min(zip(prefs,populations),key=lambda x: x[1]))   #ラムダ式でキーを指定
print(max(zip(prefs,populations),key=lambda x: x[1]))