import pandas as pd
from pyecharts import Bar

df = pd.read_csv('Best_Actress_LR.csv', header=None, names=['year', 'win', 'nomination'], encoding='gbk')

people_all, people_once = [[], []]

for i in df['nomination']:
    for j in i.split(' '):
        people_all.append(j)

for k in df['win']:
    people_all.append(k)

for people in people_all:
    if people not in people_once:
        people_once.append(people)

names, num_1, num_2 = [[], [], []]

for p1 in people_once:
    num1, num2 = 0, 0
    for p2 in people_all:
        if p2 == p1:
            num1 += 1
    for p3 in df['win']:
        if p3 == p1:
            num2 -= 1
        else:
            pass
    # print(p1, num1, num2)
    names.append(p1)
    num_1.append(num1)
    num_2.append(num2)

data = {
    'name': names,
    'num1': num_1,
    'num2': num_2
}
frame = pd.DataFrame(data)
frame1 = frame.sort_values(by=['num1'], ascending=False)[:15]
print(frame1)

attr = frame1['name']
v1 = frame1['num1']
v2 = frame1['num2']

bar = Bar("奥斯卡最佳女主角-提名统计", title_pos='center', title_top='18', width=800, height=400)
bar.add("提名", attr, v1, is_stack=True, is_label_show=True, xaxis_rotate=30, is_legend_show=True, legend_pos="74%", legend_top="7%")
bar.add("获奖", attr, v2, is_stack=True, is_label_show=True, xaxis_rotate=30, label_pos='bottom', is_legend_show=True, legend_pos="74%", legend_top="7%")
bar.render("奥斯卡最佳女主角-提名统计.html")
