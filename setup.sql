CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR (45),
    last_name VARCHAR (45),                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    hobbies TEXT,
    active BOOLEAN DEFAULT 1
);

INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "John",
    "Doe",
    "Playing golf"
);
INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "Jane",
    "Doe",
    "Playing tennis"
);
INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "Bob",
    "Robertson",
    "Watching movies"
);


CREATE TABLE vehicle (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR (45),
    last_name VARCHAR (45),                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    make TEXT,
    model TEXT
    active BOOLEAN DEFAULT 1
);

INSERT INTO vehicle (
    first_name,
    last_name,
    make,
    model

) VALUES (
    "John",
    "Doe",
    "Smart car",
    "Fortwo"
);
INSERT INTO vehicle (
    first_name,
    last_name,
    make,
    model
    
) VALUES (
    "Jane",
    "Doe",
    "GMC",
    "Hummer_H3"
);
INSERT INTO vehicle (
    first_name,
    last_name,
    make,
    model
    
) VALUES (
    "Bob",
    "Robertson",
    "Jeep",
    "Wrangler"
);