PRAGMA foreign_keys = ON;

create table if not exists shops(id int primary key, name TEXT);
create table if not exists dates(id int primary key, date TEXT);
create table if not exists kinds(id int primary key, kind TEXT);
create table if not exists customers(id int primary key, name TEXT);

create table if not exists main(id int primary key, shop_id int, kind_id int,
                                date_id int, customer_id int, applesAmount int,
                                foreign key (shop_id) references shops(id),
                                foreign key (kind_id) references kinds(id),
                                foreign key (date_id) references dates(id),
                                foreign key (customer_id) references customers(id));

insert into shops values(1, "stash_shop");
insert into shops values(2, "kolesov93_shop");
insert into shops values(3, "Wallmart");
insert into shops values(4, "Ubileinyi");

insert into dates values(1, "2014-05-05");
insert into dates values(2, "2014-02-28");

insert into kinds values(1, "ranetki");
insert into kinds values(2, "nalivnoeRumyanoe");

insert into customers values(1, "stash");
insert into customers values(2, "kolesov93");
insert into customers values(3, "Quentin Tarantino");
insert into customers values(4, "Robert Rodrigezzz");

insert into main values(1, 1, 1, 1, 1, 10); -- stash93_shop ranetki 2014-05-05 stash

insert into main values(2, 2, 2, 2, 2, 20); -- kolesov93_shop nalivnoeRumyanoe 2014-02-28 kolesov93
insert into main values(3, 2, 1, 2, 2, 20); -- kolesov93_shop ranetki 2014-02-28 kolesov93
insert into main values(4, 3, 1, 2, 2, 20); -- Wallmart ranetki 2014-02-28 kolesov93

insert into main values(5, 1, 1, 2, 2, 30); -- stash93_shop ranetki 2014-02-28 kolesov93
insert into main values(6, 1, 1, 1, 1, 30); -- stash93_shop ranetki 2014-05-05 stash
insert into main values(7, 1, 2, 1, 1, 10); -- stash93_shop nalivnoeRumyanoe 2014-05-05 stash

insert into main values(8, 1, 1, 1, 3, 10); -- stash93_shop ranetki 2014-05-05 Quentin Tarantino


