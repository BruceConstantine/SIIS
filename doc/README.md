## 0.功能实现初步设计

+ 全校/(学院)/专业/班级学生信息的查询

+ 全校/(学院)/专业/班级男女比例的查询

+ 学习过某一课程的学生查询以及该课程的通过率

+ 开设课程详细信息查询

+ 可以考虑将绩点查询功能加入

+ 暂不考虑第二专业的情况


## 1.SIIS数据模型

__关系图如下__

![db_relation](http://o6om1eg3i.bkt.clouddn.com/siis_db.jpg)

### 1.1 学生表(students)

id: 序号，__作为主键__ ，int，从1开始，自动增长

number: 学号，varchar(16)

name: 姓名，varchar(16)

sex: 性别，varchar(16)

grade: 年级，varchar(16)

major_id: 专业id，int

class_id: 班级id，int

level: 层次（本科），varchar(16)

length_of_schooling: 学制，varchar(16)

### 1.2 成绩表(scores)

id: 序号，__作为主键__ ，int，从1开始，自动增长

year: 学年, int

term: 学期, int

stu_id: 学生id, int

course_id: 课程id

score1: 原考分数, varchar(64) #考试分数可能为‘及格’,所以不用int

score2: 补考分数, varchar(64) #考试分数可能为‘及格’,所以不用int


### 1.3 课程表(courses)

id: 序号，__作为主键__ ，int，从1开始，自动增长

name: 课程名，varchar(64)

categorg: 类别 ，varchar(32)

power: 学分，int

### 1.4 专业表(majors)

id: 序号，__作为主键__ ，int，从1开始，自动增长

name: 专业名，varchar(64)

### 1.5 班级表(classes)

id: 序号，__作为主键__ ，int，从1开始，自动增长

name: 班级名，varchar(64)


## 2.接口定义