# mysql修改初始密码

```sql
alter user 'root'@'localhost' identified by 'ApKyLoQy38plBhK1oOv!v';
```

# mysql导入导出

## 导出

```bash
mysqldump -u root -p mydatabase > mydatabase_backup.sql
```

## 导入

```bash
mysqldump -u root -p mydatabase < mydatabase_backup.sql
```

### 导出导入示例

![image-20240523200509508](./img/image-20240523200509508.png)

# mysql用户管理

## 创建用户

```sql
create user upstream@'66.77.2.3' identified by '3rbxXzrhM8!';
```

创建一个名称为‘upstream’密码为‘3rbxXzrhM8!’的用户，允许登录范围为‘66.77.2.3’

## 授权数据库给用户


