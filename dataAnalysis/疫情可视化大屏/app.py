from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
from jieba.analyse import extract_tags
import string
import utils

app = Flask(__name__)


@app.route('/cov')
def hello_world():
    return render_template("main.html")


@app.route("/c1")
def get_c1_data():
    data = utils.get_c1_data()
    data = [data[0].to_eng_string(), data[1], data[2].to_eng_string(), data[3].to_eng_string()]
    return jsonify({"confirm":data[0],"suspect":data[1],"heal":data[2],"dead":data[3]})


@app.route("/c2")
def get_c2_data():
    res = []
    for tup in utils.get_c2_data():
        # print(tup)
        res.append({"name":tup[0],"value":int(tup[1])})
    return jsonify({"data":res})


@app.route("/l1")
def get_l1_data():
    data = utils.get_l1_data()
    day,confirm,suspect,heal,dead = [],[],[],[],[]
    for a,b,c,d,e in data[7:]:
        day.append(a.strftime("%m-%d")) #a是datatime类型
        confirm.append(b)
        suspect.append(c)
        heal.append(d)
        dead.append(e)
    return jsonify({"day":day,"confirm": confirm, "suspect": suspect, "heal": heal, "dead": dead})


@app.route("/l2")
def get_l2_data():
    data = utils.get_l2_data()
    day, confirm_add, suspect_add = [], [], []
    for a, b, c in data[7:]:
        day.append(a.strftime("%m-%d"))  # a是datatime类型
        confirm_add.append(b)
        suspect_add.append(c)
    return jsonify({"day": day, "confirm_add": confirm_add, "suspect_add": suspect_add})


@app.route("/r1")
def get_r1_data():
    data = utils.get_r1_data()
    city = []
    confirm = []
    for k,v in data:
        city.append(k)
        confirm.append(int(v))
    return jsonify({"city": city, "confirm": confirm})


@app.route("/r2")
def get_r2_data():
    data = utils.get_r2_data() #格式 (('民警抗疫一线奋战16天牺牲1037364',), ('四川再派两批医疗队1537382',)
    d = []
    for i in data:
        k = i[0].rstrip(string.digits)  # 移除热搜数字
        v = i[0][len(k):]  # 获取热搜数字
        ks = extract_tags(k)  # 使用jieba 提取关键字
        for j in ks:
            if not j.isdigit():
                d.append({"name": j, "value": v})
    return jsonify({"kws": d})


@app.route("/time")
def get_time():
    return utils.get_time()


@app.route('/ajax',methods=["get","post"])
def hello_world4():
    name = request.values.get("name")
    score =  request.values.get("score")
    print(f"name:{name},score:{score}")
    return '10000'


@app.route('/tem')
def hello_world3():
    return render_template("index.html")


@app.route('/login')
def hello_world2():
    name =  request.values.get("name")
    pwd =  request.values.get("pwd")
    return f'name={name},pwd={pwd}'


@app.route("/abc")
def hello_world1():
    id = request.values.get("id")
    return f"""
    <form action="/login">
        账号：<input name="name" value="{id}"><br>
        密码：<input name="pwd">
        <input type="submit">
    </form>
    """


if __name__ == '__main__':
    app.run()
