# url字段规定

# 登陆界面
## 字段：**\login**
json对象：
### 用户名
#### 键
username
#### 值
数据类型为 **字符串**
### 密码 
#### 键
password
#### 值
数据类型为 **数字**

# 管理员界面
## 字段：**\admin\<adminid>**
json对象：
### 管理员编号
#### 键
AdminId
#### 值
数据类型为 **数字**
### 管理员姓名
#### 键
AdminName
#### 值
数据类型为 **字符串**

# 图书管理界面
## 字段：**\admin\book**

# 图书加入管理界面
## 字段：**\admin\book\add**
json对象：
### 图书编号
#### 键
BookNum
#### 值
数据类型为 **字符串**
### 书名
#### 键
BookName
#### 值
数据类型为 **字符串**
### 作者
#### 键
Writer
#### 值
数据类型为 **字符串**
### 类别及其ID
#### 键
DortID
#### 值
数据类型为 **字符串**
### 单价
#### 键
Price
#### 值
数据类型为 **数字**
### 出版社
#### 键
PubCmopany
#### 值
数据类型为 **字符串**
### 出版日期
#### 键
PubDate
#### 值
数据类型为 **字符串**
### 总数量
#### 键
TotalNum
#### 值
数据类型为 **数字**
### 当前数量
#### 键
CurrentNum
#### 值
数据类型为 **数字**
### 内容摘要
#### 键
Brief
#### 值
数据类型为 **字符串**

# 图书加入成功界面
## 字段：**\admin\book\add\sucess**

# 图书加入失败界面
## 字段：**\admin\book\add\fail**


# 图书删除管理界面
## 字段：**\admin\book\delete**
json对象：
### 图书编号
#### 键
BookNum
#### 值
数据类型为 **字符串**
### 书名
#### 键
BookName
#### 值
数据类型为 **字符串**
### 作者
#### 键
Writer
#### 值
数据类型为 **字符串**
### 类别及其ID
#### 键
DortID
#### 值
数据类型为 **字符串**
### 单价
#### 键
Price
#### 值
数据类型为 **数字**
### 出版社
#### 键
PubCmopany
#### 值
数据类型为 **字符串**
### 出版日期
#### 键
PubDate
#### 值
数据类型为 **字符串**
### 总数量
#### 键
TotalNum
#### 值
数据类型为 **数字**
### 当前数量
#### 键
CurrentNum
#### 值
数据类型为 **数字**
### 内容摘要
#### 键
Brief
#### 值
数据类型为 **字符串**

# 图书删除成功界面
## 字段：**\admin\book\delete\sucess**

# 图书删除失败界面
## 字段：**\admin\book\delete\fail**

# 图书信息修改管理界面
## 字段：**\admin\book\modify**
json对象：
### 图书编号
#### 键
BookNum
#### 值
数据类型为 **字符串**
### 书名
#### 键
BookName
#### 值
数据类型为 **字符串**
### 作者
#### 键
Writer
#### 值
数据类型为 **字符串**
### 类别及其ID
#### 键
DortID
#### 值
数据类型为 **字符串**
### 单价
#### 键
Price
#### 值
数据类型为 **数字**
### 出版社
#### 键
PubCmopany
#### 值
数据类型为 **字符串**
### 出版日期
#### 键
PubDate
#### 值
数据类型为 **字符串**
### 总数量
#### 键
TotalNum
#### 值
数据类型为 **数字**
### 当前数量
#### 键
CurrentNum
#### 值
数据类型为 **数字**
### 内容摘要
#### 键
Brief
#### 值
数据类型为 **字符串**

# 图书信息修改成功界面
## 字段：**\admin\book\modify\sucess**

# 图书信息修改失败界面
## 字段：**\admin\book\modify\fail**

# 学生管理模块
## 字段：**\admin\student**
json对象：
### 学生编号
#### 键
AdminId
#### 值
数据类型为 **数字**
### 学生姓名
#### 键
AdminName
#### 值
数据类型为 **字符串**

# 借书证办理界面
## 字段：**\admin\student\libcard**
json对象：
### 学号
#### 键
StudentID
#### 值
**数字**
### 姓名
#### 键
StudentName
#### 值
**字符串**
### 密码
#### 键
Password
#### 值
**字符串**
### 学院ID
#### 键
AcademyID
#### 值
**字符串**
### 班级ID
#### 键
ClassID
#### 值
**字符串**
### 性别
#### 键
Sex
#### 值
**字符串**
### 电话
#### 键
Telephone
#### 值
**字符串**
### Email
#### 键
Email
#### 值
**字符串**
### 已借书数量
#### 键
LendedNum
#### 值
**数字**
### 创建日期
#### 键
CreateDate
#### 值
**字符串**

# 借书证办理成功界面
## 字段：**\admin\student\libcard\sucess**

# 借书证办理失败界面
## 字段：**\admin\student\libcard\fail**

# 借书证注销界面
## 字段：**\admin\student\libcardLogout**
json对象：
### 学号
#### 键
StudentID
#### 值
**数字**
### 姓名
#### 键
StudentName
#### 值
**字符串**
### 密码
#### 键
Password
#### 值
**字符串**
### 学院ID
#### 键
AcademyID
#### 值
**字符串**
### 班级ID
#### 键
ClassID
#### 值
**字符串**
### 性别
#### 键
Sex
#### 值
**字符串**
### 电话
#### 键
Telephone
#### 值
**字符串**
### Email
#### 键
Email
#### 值
**字符串**
### 已借书数量
#### 键
LendedNum
#### 值
**数字**
### 创建日期
#### 键
CreateDate
#### 值
**字符串**

# 借书证注销成功界面
## 字段：**\admin\student\libcardLogout\sucess**

# 借书证注销失败界面
## 字段：**\admin\student\libcardLogout\fail**

# 读者信息修改界面
## 字段：**\admin\student\libcardModify**
json对象：
### 学号
#### 键
StudentID
#### 值
**数字**
### 姓名
#### 键
StudentName
#### 值
**字符串**
### 密码
#### 键
Password
#### 值
**字符串**
### 学院ID
#### 键
AcademyID
#### 值
**字符串**
### 班级ID
#### 键
ClassID
#### 值
**字符串**
### 性别
#### 键
Sex
#### 值
**字符串**
### 电话
#### 键
Telephone
#### 值
**字符串**
### Email
#### 键
Email
#### 值
**字符串**
### 已借书数量
#### 键
LendedNum
#### 值
**数字**
### 创建日期
#### 键
CreateDate
#### 值
**字符串**

# 读者信息修改成功界面
## 字段：**\admin\student\libcardModify\sucess**

# 读者信息修改失败界面
## 字段：**\admin\student\libcardModify\fail**

# 借书证挂失界面
## 字段：**\admin\student\libcardLoss**
json对象：
### 学号
#### 键
StudentID
#### 值
**数字**
### 姓名
#### 键
StudentName
#### 值
**字符串**
### 密码
#### 键
Password
#### 值
**字符串**
### 学院ID
#### 键
AcademyID
#### 值
**字符串**
### 班级ID
#### 键
ClassID
#### 值
**字符串**
### 性别
#### 键
Sex
#### 值
**字符串**
### 电话
#### 键
Telephone
#### 值
**字符串**
### Email
#### 键
Email
#### 值
**字符串**
### 已借书数量
#### 键
LendedNum
#### 值
**数字**
### 创建日期
#### 键
CreateDate
#### 值
**字符串**

# 借书证挂失成功界面
## 字段：**\admin\student\libcardLoss\sucess**

# 借书证挂失失败界面
## 字段：**\admin\student\libcardLoss\fail**

# 借阅信息管理模块
## 字段：**\admin\borrow**

# 管理员图书检索模块
## 字段：**\admin\search**

# 学生界面
## 字段：**\student**

# 学生图书检索模块
## 字段 **\student\search**