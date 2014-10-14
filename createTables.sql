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
insert into kinds values(3, "avangard");
insert into kinds values(4, "avgusta");
insert into kinds values(5, "alpek");
insert into kinds values(6, "babyshkino");
insert into kinds values(7, "borovinko");
insert into kinds values(8, "vagner");
insert into kinds values(9, "vita");
insert into kinds values(10, "vishnevaya");
insert into kinds values(11, "gornist"); 
insert into kinds values(12, "dachnaya");
insert into kinds values(14, "dolgo");
insert into kinds values(15, "dybrovinko");
insert into kinds values(16, "zivinka");
insert into kinds values(17, "zarevo");
insert into kinds values(18, "zdorovie");
insert into kinds values(19, "imrys");
insert into kinds values(20, "kvintin");
insert into kinds values(21, "kortland");
insert into kinds values(22, "lobo");
insert into kinds values(23, "lych");
insert into kinds values(221, "malinka");
insert into kinds values(24, "malinka");
insert into kinds values(25, "mariya");
insert into kinds values(26, "nimfa");
insert into kinds values(27, "orlik");
insert into kinds values(28, "palitra");
insert into kinds values(29, "pavlysha");
insert into kinds values(30, "prima");
insert into kinds values(31, "rossa");
insert into kinds values(32, "ryblevoe");
insert into kinds values(33, "svetloe");
insert into kinds values(34, "skala");
insert into kinds values(35, "start");
insert into kinds values(36, "spartak");
insert into kinds values(37, "titovka");
insert into kinds values(38, "ytes");
insert into kinds values(39, "chara");
insert into kinds values(40, "yantar");


insert into customers values(1, "stash");
insert into customers values(2, "kolesov93");
insert into customers values(3, "Quentin Tarantino");
insert into customers values(4, "Robert Rodrigezzz");
insert into customers values(5, "ann");
insert into customers values(6, "nastya");
insert into customers values(7, "sveta");
insert into customers values(8, "pasha");
insert into customers values(9, "tolya");
insert into customers values(10, "alina");
insert into customers values(11, "igor");
insert into customers values(12, "toma");
insert into customers values(13, "valentina");
insert into customers values(14, "begemot");
insert into customers values(15, "natasha");
insert into customers values(16, "zhanna");
insert into customers values(17, "nikita");
insert into customers values(18, "vladimir");
insert into customers values(19, "vitek");
insert into customers values(20, "anton");

insert into main values(1, 1, 1, 1, 1, 10); -- stash93_shop ranetki 2014-05-05 stash

insert into main values(2, 2, 2, 2, 2, 20); -- kolesov93_shop nalivnoeRumyanoe 2014-02-28 kolesov93
insert into main values(3, 2, 1, 2, 2, 20); -- kolesov93_shop ranetki 2014-02-28 kolesov93
insert into main values(4, 3, 1, 2, 2, 20); -- Wallmart ranetki 2014-02-28 kolesov93

insert into main values(5, 1, 1, 2, 2, 30); -- stash93_shop ranetki 2014-02-28 kolesov93
insert into main values(6, 1, 1, 1, 1, 30); -- stash93_shop ranetki 2014-05-05 stash
insert into main values(7, 1, 2, 1, 1, 10); -- stash93_shop nalivnoeRumyanoe 2014-05-05 stash

insert into main values(8, 1, 1, 1, 3, 10); -- stash93_shop ranetki 2014-05-05 Quentin Tarantino


