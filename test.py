seq = [0, 4, 1, 2, 3, 5]
rev_seq = reversed(seq)  # リストを逆順にする
# リストを逆順にする

print(rev_seq)
# リスト型ではなく、専用のイテレーターが返ってくる


print(type(rev_seq))
# タイプを確認


list(rev_seq)
# リストに変換して出力
[5, 3, 2, 1, 4, 0]

list(rev_seq)
# rev_seqはイテレータなので2回目は空リストとなる
[]
print()
seq
# もとのデータは変更されていない
[0, 4, 1, 2, 3, 5]
