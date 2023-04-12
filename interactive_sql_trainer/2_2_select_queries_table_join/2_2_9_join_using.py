"""
create table author(
  author_id int primary key auto_increment,
  name_author varchar(50)
);

create table genre(
  genre_id int primary key auto_increment,
  name_genre varchar(30)
);

create table book(
  book_id int primary key auto_increment,
  title varchar(50),
  author_id int not null,
  genre_id int,
  price decimal(8, 2),
  amount int,
  foreign key (author_id) references author(author_id) on delete cascade,
  foreign key (genre_id) references genre(genre_id) on delete set null
);

create table supply(
  supply_id int primary key auto_increment,
  title varchar(50),
  author varchar(50),
  price decimal(8, 2),
  amount int
);

INSERT INTO author (name_author)
values
('Булгаков М.А.'),
('Достоевский Ф.М.'),
('Есенин С.А.'),
('Пастернак Б.Л.'),
('Лермонтов М.Ю.'),
('Пушкин А.С.')
;

INSERT INTO genre (name_genre)
values
('Роман'),
('Поэма'),
('Приключения')
;

INSERT INTO book (title, author_id, genre_id, price, amount)
VALUES
('Мастер и Маргарита', 1, 1, 670.99, 3),
('Белая гвардия', 1, 1, 540.50, 5),
('Идиот', 2, 1, 460.00, 10),
('Братья Карамазовы', 2, 1, 799.01, 3),
('Игрок', 2, 1, 480.50, 10),
('Стихотворения и поэмы', 3, 2, 650.00, 15),
('Черный человек', 3, 2, 570.20, 6),
('Лирика', 4, 2, 518.99, 10)
;

INSERT INTO supply (title, author, price, amount)
VALUES
('Доктор Живаго', 'Пастернак Б.Л.', 618.99 , 3),
('Черный человек', 'Есенин С.А.', 570.20, 6),
('Евгений Онегин ', 'Пушкин А.С.', 440.80, 5),
('Идиот', 'Достоевский Ф.М.', 360.80, 10)
;
"""


# EXAMPLE
"""
SELECT title, name_author, author_id /* имя таблицы, из которой берется author_id, указывать не обязательно*/
FROM 
    author INNER JOIN book
    USING(author_id)
;
"""

# EXAMPLE
"""
SELECT book.title, name_author
FROM 
    author 
    INNER JOIN book USING (author_id)   
    INNER JOIN supply ON book.title = supply.title and author.name_author = supply.author
    ;
"""


# SOLUTION
"""
SELECT book.title as Название, 
  name_author as Автор,
  book.amount + supply.amount as Количество
FROM 
    author 
    INNER JOIN book USING (author_id)   
    INNER JOIN supply 
    ON (book.title, author.name_author, book.price) = (supply.title, supply.author, supply.price)
;
"""