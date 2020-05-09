drop table passengers;

create table passengers(
    id serial primary key,
    lastName varchar not null,
    firstName varchar not null,
    email varchar not null,
    flight_id integer not null);