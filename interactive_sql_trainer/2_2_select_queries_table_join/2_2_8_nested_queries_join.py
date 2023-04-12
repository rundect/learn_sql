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

insert into author (name_author)
values
('Булгаков М.А.'),
('Достоевский Ф.М.'),
('Есенин С.А.'),
('Пастернак Б.Л.'),
('Лермонтов М.Ю.')
;

insert into genre (name_genre)
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
('Лирика', 4, 2, 518.99, 10),
('Герой нашего времени', 5, 3, 570.59, 2),
('Доктор Живаго', 4, 3, 740.50, 5)
;
"""


# SOLUTION
"""
SELECT title, name_author, name_genre, price, amount
FROM author 
  INNER JOIN book 
    ON author.author_id = book.author_id
  INNER JOIN genre 
    ON book.genre_id = genre.genre_id
WHERE book.genre_id IN 
    (SELECT genre_id
     FROM book
     GROUP BY genre_id
     HAVING SUM(amount) >= ALL(
       SELECT SUM(amount) 
       FROM book 
       GROUP BY genre_id
     )
    )
ORDER BY title
;
"""