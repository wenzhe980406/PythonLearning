# _*_ coding : UTF-8 _*_
# 开发人员 : ChangYw
# 开发时间 : 2019/7/31 23:33
# 文件名称 : look_up_word.PY
# 开发工具 : PyCharm
#3)
import random

import xlrd as xlrd

excel = xlrd.open_workbook('高中3500个英语单词表.xls')
sheet1 = excel.sheet_by_index(3)
words = sheet1.col_values(1,1)
meanings =sheet1.col_values(3,1)

def main_show():
    print("欢迎来到记单词时刻")
    word_num_found = int(input("请输入需要考查单词的数量（数量必须20个以及上）"))
    word_random_list = random.sample(words, word_num_found)
    word_random_list_meanings = [meanings[words.index(i)] for i in word_random_list]

    true_count = 0#对的次数
    word_error_list = []

    for i in range(word_num_found):
        word_random = random.choice(word_random_list)
        word_random_answer = random.sample(meanings, 3)
        word_answer = word_random_list_meanings[word_random_list.index(word_random)]
        word_random_answer.append(word_answer)
        random.shuffle(word_random_answer)
        print(word_random)
        print("A:{:<30}  B:{:<30}".format(word_random_answer[0], word_random_answer[1]))
        print("C:{:<30}  D:{:<30}".format(word_random_answer[2], word_random_answer[3]))
        while True:
            answer_choice = input("请输入你的答案（ABCD选择一个）").strip()
            if not answer_choice.isalpha():
                print("输入错误，请重新输入")
                continue
            else:
                break
        if "A" == answer_choice.upper():
            if word_answer == word_random_answer[0] :
                print("答对了，加油!")
                true_count += 1
            else:
                word_error_list.append([word_random,word_answer,word_random_answer[0]])
                print("答错了！加油哦\n"
                      "正确答案是：%s" % word_answer)
        elif "B" == answer_choice.upper():
            if word_answer == word_random_answer[1]:
                print("答对了，加油!")
                true_count += 1
            else:
                word_error_list.append([word_random,word_answer,word_random_answer[1]])
                print("答错了！加油哦\n"
                      "正确答案是：%s" % word_answer)
        elif "C" == answer_choice.upper():
            if word_answer == word_random_answer[2]:
                print("答对了，加油!")
                true_count += 1
            else:
                word_error_list.append([word_random,word_answer,word_random_answer[2]])
                print("答错了！加油哦\n"
                      "正确答案是：%s" % word_answer)
        elif "D" == answer_choice.upper():
            if word_answer == word_random_answer[3]:
                print("答对了，加油!")
                true_count += 1
            else:
                word_error_list.append([word_random,word_answer,word_random_answer[3]])
                print("答错了！加油哦\n"
                      "正确答案是：%s"%word_answer)
    #测试数量：100 正确：70 错误：30 正确率：70%
    print("测试数量: %d  正确: %d  错误: %d  正确率: %.2f"%(word_num_found,true_count,word_num_found-true_count,true_count/word_num_found))
    error_choice = input("是否查看选错的单词（y/n）")
    if "Y" == error_choice :
        for i in word_error_list:
            print("你选错的单词是：%s\n"
                  "正确答案是：%s\t\t你选的是：%s"%(i[0],i[1],i[2]))
    elif "N" == error_choice:
        exit(0)





if __name__ == '__main__':
    main_show()