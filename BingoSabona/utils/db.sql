create database game

create table user(
    id int primary key auto increment,
    name varchar(255),
    email varchar(255),
    psd varchar(255)
);

create table verCode(
    id_Ver int primary key,
    email varchar (30),
    code varchar(10)
);

create table playNow(
    id int primary key auto increment,
    email varchar(30)
)