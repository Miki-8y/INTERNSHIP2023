def is_valid(s)
    flag = true
    str_list = []
    str_map = {')' => '(', ']' => '[', '}' => '{'}

    s.each_char do |char|
        if str_map.values.include?(char)
            str_list.push(char)
        elsif str_map.keys.include?(char)
            if str_list.empty? || str_map[char] != str_list.pop
                return !flag
            end
        end
    end

    flag
end

# テストする文字列定義
test_str = ['()', '([]){}', '({)}']

test_str.each do |char|
    puts "入力文字列：#{char}"
    puts "判定結果　：#{is_valid(char)}"
end