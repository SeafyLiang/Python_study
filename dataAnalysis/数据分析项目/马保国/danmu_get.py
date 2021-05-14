from bilibili_api import video, Verify
import datetime

# 参数
verify = Verify("你的SESSDATA值", "你的bili_jct值")

# 获取存在历史弹幕的日期列表
days = video.get_history_danmaku_index(bvid="BV1HJ411L7DP", verify=verify)
print(days)

# 获取弹幕信息，并保存
for day in days:
    danmus = video.get_danmaku(bvid="BV1HJ411L7DP", verify=verify, date=datetime.date(*map(int, day.split('-'))))
    print(danmus)

    f = open(r'danmu.txt', 'a')
    for danmu in danmus:
        print(danmu)
        f.write(danmu.text + '\n')
    f.close()