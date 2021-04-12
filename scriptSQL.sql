Create database: DATAcollection
CREATE TABLE books (
             book_name VARCHAR(100) NOT NULL PRIMARY KEY,
             author VARCHAR(40) NOT NULL,
             statut VARCHAR(20) NOT NULL,
             déposé_par SMALLINT NOT NULL,
             emprunté_par SMALLINT NOT NULL,
             catégorie VARCHAR(50) ,
              
)

CREATE TABLE Infos(
             book_name VARCHAR(100) NOT NULL,
             Email VARCHAR(100) NOT NULL,
             b_Description TEXT,
             Rating SMALLINT,
             PRIMARY KEY(book_name)
)

CREATE TABLE Users(
             user VARCHAR(100) NOT NULL,
             passwd VARCHAR(100) NOT NULL,
             ID INT NOT NULL
)

-- insertion de qlqs donnees f books
INSERT INTO books VALUES ('40' , 'Ahmed Shugeiri' , 'dispo', 2584 ,'AL' , 'Biographie') ;
INSERT INTO books VALUES ('The Making of a Navy SEAL' , 'Brandon Webb ' , 'dispo', 7159 ,'DO' , 'Biographie') ;
INSERT INTO books VALUES ('une chambre à soi' , 'Virginia Woolf ' , 'non disponible', 2486 ,'JB' , 'Fiction') ;
INSERT INTO books VALUES ('Antigone' , 'Jean Anouilh ' , 'dispo', 1782 ,'JK' , 'Tragédie') ;
INSERT INTO books VALUES ("dernier jour d'un condamné" , 'Victor Hugo ' , 'dispo', 4327 ,'RM' , 'Roman') ;
INSERT INTO books VALUES ("Le complot contre l'Amérique" , 'Philip Roth' , 'dispo', 2486 ,'DO' , 'Histoire') ;
INSERT INTO books VALUES ("La peste" , 'Albert Camus' , 'non disponible', 4327 ,'RM' , 'Conte philosophique') ;
INSERT INTO books VALUES ("L'étranger" , 'Albert Camus' , 'dispo', 2154 ,'AL' , 'Conte philosophique,fiction') ;
INSERT INTO books VALUES ("The Feynman Lectures on Physics" , 'Richard Feynman' , 'non disponible', 1467 ,'DK' , 'Scientifique') ;
INSERT INTO books VALUES ("Cosmos" , 'Carl Sagan' , 'non disponible', 1466 ,'MK' , 'Scientifique') ;
INSERT INTO books VALUES ("Pale Blue Dot: A Vision of the Human Future in Space" , 'Carl Sagan' , 'dispo', 1466 ,'MK' , 'Scientifique') ;


-- insertion de qlqs donnees f infos
INSERT INTO infos VALUES ( "The Making of a Navy SEAL" , "jihane.bd@gmail.com", "Webb describes how he survived military training to later become the Course Manager of the Navy SEAL Sniper Program. The book was adapted for a younger audience from Webb’s adult book The Red Circle. It was nominated for the 2018 Evergreen Teen Book Award. Webb trained Luttrell as a sniper, and Luttrell now ranks as one of the finest snipers in the U.S." , 4);


INSERT INTO infos (title, Email, b_description, rating)
 VALUES
 ('une chambre à soi ', 'kaoutarmim@gmail.com', 'Virginia Woolf analyse avec ironie les causes du silence littéraire des femmes pendant de nombreuses décennies. ', 3),
 (' Antigone', 'azharelbagahzaoui@gmail.com', 'Après Sophocle, Jean Anouilh reprend le mythe d"Antigone. Fille d"Oedipe et de Jocaste, la jeune Antigone est en révolte contre la loi humaine qui interdit d"enterrer le corps de son frère Polynice. ', 4),
 (' dernier jour d"un condamné', 'soumiyarazzouk@gmail.com', 'Le Dernier Jour d’un condamné est un roman à thèse de Victor Hugo publié en 1829 chez Charles Gosselin, qui constitue un plaidoyer politique pour l"abolition de la peine de mort. ', 2.5),
 (' Le complot contre l"Amérique', 'oumaimaboussetta@gmail.com', 'Le Complot contre l"Amérique1 est une uchronie se déroulant dans les années 1940 aux États-Unis. Le narrateur, qui porte le nom de Philip Roth, décrit ses souvenirs d"enfant issu d"une famille juive du New Jersey. ', 4.5),
 ('La peste', 'jihaneboudhen@gmail.com', 'L"histoire se déroule dans les années 1940. Elle a pour théâtre Oran durant la période de l’Algérie française. ', 2.5),
 (' L"étranger', 'MK@gmail.com', ' Il prend place dans la tétralogie que Camus nommera « cycle de l’absurde » qui décrit les fondements de la philosophie camusienne : l’absurde. ', 2),
 (' The Feynman Lectures on Physics', 'JB@gmail.com', 'Le premier traite essentiellement de la mécanique, de l"optique, des radiations lumineuses, et de la thermodynamique (théorie de la chaleur).', 4),
 (' Cosmos', 'originalfake@gmail.com', 'Une série de réflexions sur le monde qui déroule autour de 5 grands thèmes - Le temps, La vie, l"animal, le cosmos et le sublime. ', 5),
 (' Pale Blue Dot: A Vision of the Human Future in SPACE ', 'MB@gmail.com', 'A Vision of the Human Future in Space ', 1);