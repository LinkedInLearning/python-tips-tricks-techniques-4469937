prefs = ['富山県', '石川県', '福井県','岐阜県']

prefs.reverse() #  リスト自身を逆順に並び替える
print(prefs)
print(type(prefs))  #<class 'list'>


for pref in reversed(prefs):    #逆順に並び替えた結果を返す
    print(pref)

prefs_r = reversed(prefs)
print(type(prefs_r))    #<class 'list_reverseiterator'>
