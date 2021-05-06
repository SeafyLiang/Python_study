import requests
import pymysql
import random
import time
import json

count = 0
# 请求网址及请求头参数
url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Cookie': '你的Cookie值',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Connection': 'keep-alive',
    'Host': 'www.lagou.com',
    'Origin': 'https://www.lagou.com',
    'Referer': 'ttps://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?labelWords=sug&fromSearch=true&suginput=shuju'
}

# 连接数据库
db = pymysql.connect(host='127.0.0.1', user='root', password='774110919', port=3306, db='lagou_job', charset='utf8mb4')


def add_Mysql(id, job_title, job_salary, job_city, job_experience, job_education, company_name, company_type, company_status, company_people, job_tips, job_welfare):
    # 将数据写入数据库中
    try:
        cursor = db.cursor()
        sql = 'insert into job(id, job_title, job_salary, job_city, job_experience, job_education, company_name, company_type, company_status, company_people, job_tips, job_welfare) values ("%d", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")' % (id, job_title, job_salary, job_city, job_experience, job_education, company_name, company_type, company_status, company_people, job_tips, job_welfare);
        print(sql)
        cursor.execute(sql)
        print(cursor.lastrowid)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()


def get_message():
    for i in range(1, 31):
        print('第' + str(i) + '页')
        time.sleep(random.randint(10, 20))
        data = {
            'first': 'false',
            'pn': i,
            'kd': '数据分析'
        }
        response = requests.post(url=url, data=data, headers=headers)
        result = json.loads(response.text)
        job_messages = result['content']['positionResult']['result']
        for job in job_messages:
            global count
            count += 1
            # 岗位名称
            job_title = job['positionName']
            print(job_title)
            # 岗位薪水
            job_salary = job['salary']
            print(job_salary)
            # 岗位地点
            job_city = job['city']
            print(job_city)
            # 岗位经验
            job_experience = job['workYear']
            print(job_experience)
            # 岗位学历
            job_education = job['education']
            print(job_education)
            # 公司名称
            company_name = job['companyShortName']
            print(company_name)
            # 公司类型
            company_type = job['industryField']
            print(company_type)
            # 公司状态
            company_status = job['financeStage']
            print(company_status)
            # 公司规模
            company_people = job['companySize']
            print(company_people)
            # 工作技能
            if len(job['positionLables']) > 0:
                job_tips = ','.join(job['positionLables'])
            else:
                job_tips = 'None'
            print(job_tips)
            # 工作福利
            job_welfare = job['positionAdvantage']
            print(job_welfare + '\n\n')
            # 写入数据库
            add_Mysql(count, job_title, job_salary, job_city, job_experience, job_education, company_name, company_type, company_status, company_people, job_tips, job_welfare)


if __name__ == '__main__':
    get_message()