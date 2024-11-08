# 创建系统用户密码

```sql
\password passwordname
```

# 创建用户并设置密码
```sql
CREATE USER username WITH PASSWORD 'passwordname';
```

# 创建数据库

```sql
CREATE DATABASE databasename OWNER dbuser;
```

# 赋予用户操作权限

```sql
GRANT ALL PRIVILEGES ON DATABASE databasename to dbuser;
```

# 创建表格

```sql
CREATE TABLE tablename(
    ID INT PRIMARY KEY NOT NULL;
    ID_FOR_USER INT NOT NULL;
);
```

# 创建SCHEMA

```sql
CREATE SCHEMA schemaname;
```
