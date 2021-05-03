import psycopg2
# 连接数据库
conn = psycopg2.connect(database="lagou_job", user="postgres", password="774110919", host="127.0.0.1", port="5432")
print("Opened database successfully")
# 创建工作表
cur = conn.cursor()
cur.execute('''CREATE TABLE job (id INT PRIMARY KEY NOT NULL, job_title TEXT NOT NULL, job_salary TEXT NOT NULL, job_city TEXT NOT NULL, job_experience TEXT NOT NULL, job_education TEXT NOT NULL, company_name TEXT NOT NULL, company_type TEXT NOT NULL, company_status TEXT NOT NULL, company_people TEXT NOT NULL, job_tips TEXT NOT NULL, job_welfare TEXT NOT NULL);''')
print("Table created successfully")
# 关闭数据库
conn.commit()
conn.close()

