# 1

my_favorite_artist = ["いきものがかり", "マイケルジャクソン", "bigbang", "kara"]

# 2

location = [(35.1814, 136.9063), (35.0116, 135.768), (35.6895, 139.6917)]

# 3

my_info = {
    "address": "Nagoya",
    "tel": "080-8753-9628",
    "favorite_color": "red",
}

# 4 
string = input("キーを入力してください：")
if string in my_info:
    string = my_info[string]
    print(string)
else:
    print("正しくありません。")

# 5
my_favorite_artist_dic = {"kara": ["Go Go summer", "jumpin", "jetcoster love"]}

# 6
# set() 
# セットを生成する際には重複する要素は取り除かれます。
# また、ディクショナリからセットを生成すると、キーがセットの要素となります。
