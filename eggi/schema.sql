DROP TABLE IF EXISTS subscription;
DROP TABLE IF EXISTS version;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS library;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL  
);

CREATE TABLE library (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE subscription (
    user_id INTEGER NOT NULL,
    library_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user (id),
    FOREIGN KEY (library_id) REFERENCES library (id)
);

CREATE TABLE version (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    commit_hash TEXT NOT NULL,
    version TEXT NOT NULL,
    changelog TEXT NOT NULL,
    library_id INTEGER NOT NULL,
    FOREIGN KEY (library_id) REFERENCES library (id),
    CONSTRAINT UC_version UNIQUE (library_id, version)
);