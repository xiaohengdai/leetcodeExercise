# SQL练习:https://blog.csdn.net/zzti_erlie/article/details/79440432

学号:sid
姓名:sname
课:cid
成绩:score
student(sid,sname,sage,ssex) 学生表 
course(cid,cname,tid) 课程表 
sC(sid,cid,score) 成绩表 

1.查询所有同学的学号、姓名、选课数、总成绩
select student.sid,student.sname,sC.cid,sum(score) from student left join  sC student.sid=sC.sid group by student.sid; 

2.查询平均成绩大于60分的同学的学号和平均成绩 (s_id,score,sc)
select s_id,avg(score) from sc group by s_id having avg(score)>60;


