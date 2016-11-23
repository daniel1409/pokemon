create table moves (
    id int not null,
    move varchar(255), 
    description varchar(255),
    type varchar(255),
    category varchar(255),
    power varchar(255),
    accuracy varchar(255),
    pp varchar(255),
    zeffect varchar(255),
    priority varchar(255),
    crit varchar(255),
    primary key(id)
);