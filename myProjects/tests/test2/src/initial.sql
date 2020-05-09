drop table accounts;
drop table transactions;

create table accounts(
    id serial primary key,
    email varchar not null,
    passwd varchar not null
);

create table transactions(
    id serial primary key,
    account_id integer not null,
    amount float
);

ALTER TABLE transactions add constraint account_id_constraint foreign key (account_id) references accounts;