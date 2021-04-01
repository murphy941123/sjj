import pymysql
# 获取验证码

sql = 'SELECT mobile ,content ,gmt_create from crm_user_sms where (mobile=18100000001) order by id desc limit 1'
conn = pymysql.connect(host='rm-m5e3kq2fg7k4jy343qo.mysql.rds.aliyuncs.com', user='chenli',
                               password='Cqtouch2014', database='booklnbak')
cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
cur.execute(sql)
result = cur.fetchall()
# print(result)

sms_code = result[0]['content']
print(sms_code)
# i=-1

# while i<4:
#     i = i + 1
#     r=int(sms_code[i])+7
    # print(r)



