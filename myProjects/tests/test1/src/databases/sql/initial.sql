drop table flights;

create table flights(
    id serial primary key,
    origin varchar not null,
    destination varchar not null,
    duration varchar not null
);

drop table passengers;

create table passengers(
    id serial primary key,
    lastName varchar not null,
    firstName varchar not null,
    email varchar not null,
    flight_id integer not null);

ALTER TABLE passengers add constraint flight_id_constraint foreign key (flight_id) references flights;