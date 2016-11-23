create table natures (
    id serial not null,
    nature varchar(255), 
    attack varchar(10),
    defense varchar(10),
    spattack varchar(10),
    spdefense varchar(10),
    speed varchar(10),
    primary key(id)
);