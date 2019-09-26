create table post (
    id serial,
    title varchar(255) not null,
    body text
);

insert into post(title, body) values ('First post', 'This is HELLO post');
insert into post(title, body) values ('Second post', 'Hello Dimasik');