drop table if exists twlo;
create table twlo(
  id integer primary key autoincrement,
  datetime timestamp not null,
  price numeric not null)
