drop table flights;

create table flights(
    id serial primary key,
    origin varchar not null,
    destination varchar not null,
    duration varchar not null
);