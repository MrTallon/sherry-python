import pandas as pd
from sqlalchemy import create_engine

# 创建数据库连接
engine = create_engine(
    "mysql+pymysql://root:RbezMkXC4ftJAqNGygYrytRZ@rm-2zeupxx1363eo3cnh.mysql.rds.aliyuncs.com/teaching_main")

# 使用pandas读取数据
df = pd.read_sql("select * from agent", engine)

# 显示数据
print(df)
