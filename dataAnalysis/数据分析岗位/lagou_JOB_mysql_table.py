import pymysql

db = pymysql.connect(host='127.0.0.1', user='root', password='774110919', port=3306, db='lagou_job')
cursor = db.cursor()
sql = 'CREATE TABLE IF NOT EXISTS job (id INT NOT NULL, job_title VARCHAR(255) NOT NULL, job_salary VARCHAR(255) NOT NULL, job_city VARCHAR(255) NOT NULL, job_experience VARCHAR(255) NOT NULL, job_education VARCHAR(255) NOT NULL, company_name VARCHAR(255) NOT NULL, company_type VARCHAR(255) NOT NULL, company_status VARCHAR(255) NOT NULL, company_people VARCHAR(255) NOT NULL, job_tips VARCHAR(255) NOT NULL, job_welfare VARCHAR(255) NOT NULL, PRIMARY KEY (id))'
cursor.execute(sql)
db.close()
