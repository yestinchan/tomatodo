create table todos(
    id int(10) auto_increment primary key,
    content varchar(500) not null,
    user_id int(10) not null,
    created datetime ,
    started datetime,
    finished datetime,
    broken int(1),
    interrupt int(5)
);

create table user(
    id int(10) auto_increment primary key,
    password varchar(200) not null,
    registered datetime
);

create table todaylist(
    todo_id int(10),
    added datetime,
    total_tomato int(5),
    used_tomato int(5)
);