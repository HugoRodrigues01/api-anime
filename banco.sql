-- SQLite3

CREATE TABLE tbl_type_anime (
	id_type_anime INTEGER AUTO INCREMENT,
	type_anime VARCHAR(50) NOT NULL,
	add_date_type_anime DATETIME DEFAULT CURRENT_TIMESTAMP,
	last_modifyed_date_type_anime DATETIME DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (id_type_anime),
	UNIQUE (type_anime)
);


CREATE TABLE tbl_anime (
	id_anime INTEGER AUTO INCREMENT,
	name_anime VARCHAR(50) NOT NULL,
	description_anime VARCHAR(200),
	criation_date_anime DATE NOT NULL,
	add_date_anime DATETIME DEFAULT CURRENT_TIMESTAMP,
	last_modifyed_date_anime DATETIME DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (id_anime)
);

select * from sqlite_master WHERE type='table';

INSERT INTO tbl_anime (
    id_anime, name_anime,
    description_anime,
    criation_date_anime
)
VALUES
(1, 'Dragon Ball Z', 'Anime de luta issekai', '1998-01-12'),
(2, 'Boruto', 'Continuação de naruto', '2017-10-22')
