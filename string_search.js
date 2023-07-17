function isValid(s) {
    let flag = true;
    let str_list = [];
    let str_map = {')':'(', ']':'[', '}':'{'};

    for (let char of s) {
        if (Object.values(str_map).includes(char)) {
            str_list.push(char);
        } else if (Object.keys(str_map).includes(char)) {
            if ((str_list.length === 0) || (str_map[char] !== str_list.pop())) {
                return !flag;
            }
        }
    }
    return flag;
}

// テストする文字列定義
let test_str = ['()', '([]){}', '({)}'];

for (let char of test_str) {
    console.log(`入力文字列：${char}`);
    console.log(`判定結果　：${isValid(char)}`);
}