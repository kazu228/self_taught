# 1

string1 = "カミュ"
for i in range(len(string1)):
    print(string1[i])

# 2

a = input("文字列を入力してください。：")
b = input("文字列を入力してください。：")

result = "私は昨日{0}を書いて、{1}に送った！".format(a,b)
print(result)

# 3
string2 = "aldous Huxley was born in 1894."
print(string2.capitalize())

# 4
string3 = "どこで？　だれが？　いつ？"
print(string3.split())

# 5
fox = ["The", "fox", "jumped", "over", "the", "fence", "."]
string4 = " ".join(fox[0:7])
string4 = string4[0: -2] + "."
print(string4)

# 6
sentence = "A screaming comes across the sky."
sentence = sentence.replace("s", "$")
print(sentence)

# 7
index = "Hemingway".index("m")
print(index)

# 8
print("俺は、\"こんなん\"じゃない")

# 9
print("three " + "three " + "three")
print("three " * 3)

# 10
string5 = "四月の晴れた寒い日で、時計がどれも十三時を打っていた。"
string5 = string5.split("、")
print(string5[0])
