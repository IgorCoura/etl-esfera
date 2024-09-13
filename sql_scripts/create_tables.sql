CREATE TABLE sources(
    id SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(250) NOT NULL UNIQUE
);

CREATE TABLE categories (
    id SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(250) NOT NULL UNIQUE,
    parent_category_id INTEGER,
    FOREIGN KEY (parent_category_id) REFERENCES categories(id)
);

CREATE TABLE resources(
    id SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(250) NOT NULL,
    amount NUMERIC(15, 2) NOT NULL,
    currency_code VARCHAR(3) NOT NULL, -- ISO 4217 code for currency (USD, EUR, BRL)
    category_id INTEGER NOT NULL,
    source_id INTEGER NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(id),
    FOREIGN KEY (source_id) REFERENCES sources(id)
);


