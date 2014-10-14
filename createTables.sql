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
insert into shops values(5, "Zhivinka");
insert into shops values(6, "Petrovskyi");
insert into shops values(7, "Fatumin");
insert into shops values(8, "Fryktu");
insert into shops values(9, "Agroles");
insert into shops values(10, "Osobyi");
insert into shops values(11, "Vitanova");
insert into shops values(12, "Zelenyi Klen");
insert into shops values(13, "TorgPin");
insert into shops values(14, "Ryblevskiy");
insert into shops values(15, "Sosedi");
insert into shops values(16, "Evroopt");
insert into shops values(17, "Evrotorg");
insert into shops values(18, "SelHozProdyctu");
insert into shops values(19, "Palesse");
insert into shops values(20, "Yrozhai");

insert into dates values(1, "2014-05-05");
insert into dates values(2, "2014-02-28");
insert into dates values(3, "2013-12-01");
insert into dates values(4, "2010-06-18");
insert into dates values(5, "2002-07-11");
insert into dates values(6, "2012-04-01");
insert into dates values(7, "2013-11-21");
insert into dates values(8, "2011-08-23");
insert into dates values(9, "2002-09-11");
insert into dates values(10, "2003-01-15");
insert into dates values(11, "2009-02-09");
insert into dates values(12, "2011-07-17");
insert into dates values(13, "2012-10-30");
insert into dates values(14, "2009-11-03");
insert into dates values(15, "2001-03-19");
insert into dates values(16, "2008-09-22");
insert into dates values(17, "2011-04-24");
insert into dates values(18, "2012-03-25");
insert into dates values(19, "2014-01-11");
insert into dates values(20, "2013-07-10");

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
insert into kinds values(231, "malinka");
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

insert into main values(81, 2, 3, 3, 3, 20);
insert into main values(9, 2, 3, 5, 6, 10);
insert into main values(10, 1, 10, 11, 13, 10);
insert into main values(11, 6, 4, 12, 5, 50);
insert into main values(12, 8, 11, 17, 9, 15);
insert into main values(14, 2, 18, 5, 11, 10);
insert into main values(15, 19, 5, 6, 3, 25);
insert into main values(16, 14, 3, 6, 13, 10);
insert into main values(17, 14, 11, 5, 15, 15);
insert into main values(18, 17, 12, 20, 18, 20);
insert into main values(19, 15, 8, 11, 17, 40);
insert into main values(20, 10, 9, 19, 19, 30);
insert into main values(21, 13, 10, 18, 20, 50);
insert into main values(22, 13, 7, 15, 2, 15);
insert into main values(23, 19, 17, 12, 4, 25);
insert into main values(24, 11, 20, 2, 5, 35);
insert into main values(26, 19, 11, 4, 6, 45);
insert into main values(27, 19, 3, 6, 8, 5);
insert into main values(28, 13, 4, 8, 10, 10);
insert into main values(29, 12, 19, 10, 12, 20);
insert into main values(30, 3, 7, 12, 14, 30);
insert into main values(31, 9, 9, 14, 16, 40);
insert into main values(32, 3, 7, 16, 17, 50);
insert into main values(33, 2, 8, 18, 18, 5);
insert into main values(34, 19, 10, 20, 20, 15);
insert into main values(35, 2, 11, 1, 1, 15);
insert into main values(36, 4, 20, 3, 3, 25);
insert into main values(37, 5, 1, 5, 5, 35);
insert into main values(38, 10, 2, 7, 7, 45);
insert into main values(39, 11, 6, 11, 9, 50);
insert into main values(40, 14, 17, 13, 11, 10);
insert into main values(41, 13, 7, 1, 13, 20);
insert into main values(42, 11, 5, 17, 15, 30);
insert into main values(43, 9, 4, 19, 17, 40);
insert into main values(44, 16, 11, 2, 19, 50);
insert into main values(45, 6, 1, 3, 2, 5);
insert into main values(46, 13, 3, 4, 4, 15);
insert into main values(47, 1, 4, 6, 6, 25);
insert into main values(48, 10, 5, 8, 8, 35);
insert into main values(49, 11, 2, 10, 10, 45);
insert into main values(50, 6, 11, 12, 12, 10);
insert into main values(51, 9, 18, 14, 14, 20);
insert into main values(52, 19, 17, 16, 16, 30);
insert into main values(53, 7, 16, 18, 18, 40);
insert into main values(54, 8, 20, 20, 20, 50);
insert into main values(55, 1, 1, 1, 2, 5);
insert into main values(56, 12, 8, 3, 1, 15);
insert into main values(57, 18, 5, 5, 3, 25);
insert into main values(58, 8, 2, 7, 5, 35);
insert into main values(59, 9, 4, 9, 7, 45);
insert into main values(60, 14, 12, 11, 9, 50);
insert into main values(61, 9, 11, 12, 1, 10);
insert into main values(62, 11, 3, 15, 13, 20);
insert into main values(63, 10, 18, 17, 15, 30);
insert into main values(64, 19, 14, 19, 17, 40);
insert into main values(65, 1, 17, 2, 19, 50);
insert into main values(66, 6, 9, 4, 2, 40);
insert into main values(67, 4, 20, 6, 4, 30);
insert into main values(68, 5, 1, 8, 6, 20);
insert into main values(69, 17, 18, 10, 8, 10);
insert into main values(70, 18, 4, 12, 10, 5);
insert into main values(71, 15, 5, 14, 12, 15);
insert into main values(72, 13, 6, 16, 14, 25);
insert into main values(73, 2, 11, 18, 16, 35);
insert into main values(74, 12, 18, 20, 18, 45);
insert into main values(75, 11, 19, 1, 20, 35);
insert into main values(76, 10, 11, 3, 1, 25);
insert into main values(77, 19, 1, 5, 3, 15);
insert into main values(78, 17, 2, 7, 5, 5);
insert into main values(79, 16, 9, 9, 7, 10);
insert into main values(80, 8, 10, 11, 9, 20);
insert into main values(810, 17, 10, 13, 11, 30);
insert into main values(82, 11, 11, 15, 13, 40);
insert into main values(83, 19, 12, 17, 15, 50);
insert into main values(84, 13, 6, 19, 17, 50);
insert into main values(85, 12, 7, 2, 19, 40);
insert into main values(86, 12, 9, 4, 2, 30);
insert into main values(87, 10, 2, 6, 4, 20);
insert into main values(88, 11, 17, 8, 6, 10);
insert into main values(89, 11, 15, 10, 8, 5);
insert into main values(90, 11, 11, 12, 10, 15);
insert into main values(91, 12, 12, 14, 12, 25);
insert into main values(92, 10, 9, 16, 14, 25);
insert into main values(93, 18, 8, 18, 16, 35);
insert into main values(94, 10, 2, 20, 18, 45);
insert into main values(95, 14, 6, 1, 20, 35);
insert into main values(96, 17, 3, 3, 1, 25);
insert into main values(97, 18, 12, 1, 3, 15);
insert into main values(98, 7, 14, 4, 1, 5);
insert into main values(99, 19, 20, 7, 7, 10);
insert into main values(100, 4, 1, 8, 9, 20);
insert into main values(101, 1, 19, 9, 11, 30);
insert into main values(102, 8, 9, 10, 13, 40);
insert into main values(103, 6, 2, 12, 15, 50);
insert into main values(104, 13, 10, 14, 17, 50);
insert into main values(105, 14, 12, 16, 19, 40);
insert into main values(106, 17, 19, 18, 2, 30);
insert into main values(107, 5, 14, 20, 4, 20);
insert into main values(108, 11, 11, 1, 6, 10);
insert into main values(109, 7, 1, 3, 8, 5);
insert into main values(110, 12, 2, 5, 10, 15);
insert into main values(111, 11, 10, 7, 12, 25);
insert into main values(112, 4, 9, 9, 14, 35);
insert into main values(113, 1, 11, 11, 16, 45);
insert into main values(114, 7, 3, 13, 18, 45);
insert into main values(115, 6, 1, 15, 20, 35);
insert into main values(116, 19, 6, 17, 1, 25);
insert into main values(117, 11, 14, 19, 3, 15);
insert into main values(118, 18, 16, 2, 5, 5);
insert into main values(119, 6, 20, 3, 7, 10);
insert into main values(120, 7, 1, 4, 9, 20);



