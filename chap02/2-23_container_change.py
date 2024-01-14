scores = {'network':60, 'database':80, 'security':60}
members = ['松田', '浅木', '工藤']
print(tuple(members))       # リストmembersをタプルに変換して表示
key = list(scores)
print(list(scores))         # scoresのキーをリストに変換して表示
value = list(scores.values())
print(set(scores.values())) # scoresの値をセットに変換して表示
print(dict(zip(key, value)))