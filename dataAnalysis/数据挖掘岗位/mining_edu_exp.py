import statsmodels.formula.api as smf
import statsmodels.api as sm
import pandas as pd
import psycopg2
# 消除pandas输出省略号情况及换行情况
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
# 获取数据库数据
conn = psycopg2.connect(database="lagou_job", user="postgres", password="774110919", host="127.0.0.1", port="5432")
cursor = conn.cursor()
sql = "select * from job"
df = pd.read_sql(sql, conn)
# 清洗数据,生成薪水列
dom = []
for i in df['job_salary']:
    i = ((float(i.split('-')[0].replace('k', '').replace('K', '')) + float(i.split('-')[1].replace('k', '').replace('K', ''))) / 2) * 1000
    dom.append(i)
df['salary'] = dom
# 去除学历不限
data = df[df.job_education != '不限']
# 去除工作经验不限及1年以下
data = data[data.job_experience != '不限']
data = data[data.job_experience != '1年以下']
# smf:最小二乘法,构建线性回归模型
anal = smf.ols('salary ~ C(job_experience) + C(job_education) + C(job_experience)*C(job_education)', data=data).fit()
# anova_lm:多因素方差分析
print(sm.stats.anova_lm(anal))
# 基本信息输出
print(anal.summary())