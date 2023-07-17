#引数文字列s，返り値bool(TrueかFaulseの二値)
def isValid(s: str) -> bool:
    flag = True
    str_list = []
    #開き括弧と閉じ括弧を辞書で対応付ける
    str_map = {')':'(', ']':'[', '}':'{'}
    
    for char in s:
        if char in str_map.values():
            str_list.append(char)
        elif char in str_map.keys():
            #判定1つ目 -> 「)]}」だけの場合に対応
            #判定2つ目 -> 「({)」等に対応（最後に追加された括弧が対応する開き括弧と一致しない場合に対応）
            if ((str_list == []) or (str_map[char] != str_list.pop())):
                return not flag
    return flag

#テストする文字列定義
test_str = ['()','([]){}','({)}',]

for char in test_str:
    print(f"入力文字列：{char}")
    print(f"判定結果　：{isValid(char)}")