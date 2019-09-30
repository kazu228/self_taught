# 1

list = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
for item in list:
    print(item)

# 2
i = 25
while i <= 50:
    print(i)
    i += 1

# 3
for i, item in enumerate(list):
    print(str(i) + ":" + item)

# 4
number_list = [0, 50, 72, 100]
while True:
    k = input("文字を入力してください：")
    if k == "q":
        break
    if k.isalpha() == True:
        print("数字を入力するか、ｑで終了します。")
        continue
    for num in number_list:
        if k == str(num):
            print("正解です。")
        else:
            print("不正解です")

    # try:
    #     k = int(k)
    # except  ValueError:
    #     print("数字を入力するか、ｑで終了します。")
    # if num in number_list:
    #     print("正解です。")
    # else:
    #     print("不正解です")

# 5
list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
new_list = []

for x in list1:
    for y in list2:
        b = x * y
        new_list.append(b)
print(new_list)