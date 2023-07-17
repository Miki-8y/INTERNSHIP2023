fun isValid(s: String): Boolean {
    var flag = true
    val strList = mutableListOf<Char>()
    val strMap = mapOf(')' to '(', ']' to '[', '}' to '{')

    for (char in s) {
        if (char in strMap.values) {
            strList.add(char)
        } else if (char in strMap.keys) {
            if (strList.isEmpty() || strMap[char] != strList.removeAt(strList.size - 1)) {
                return !flag
            }
        }
    }

    return flag
}


fun main(){
    // テストする文字列定義
    val testStr = listOf("()", "([]){}", "({)}")
    
    for (char in testStr) {
        println("入力文字列：$char")
        println("判定結果　：${isValid(char)}")
    }
}
