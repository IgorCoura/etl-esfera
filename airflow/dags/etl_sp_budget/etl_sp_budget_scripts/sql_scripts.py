
CREATE_TABLES = """
    CREATE TABLE IF NOT EXISTS sources(
    id SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(250) NOT NULL UNIQUE
    );

    CREATE TABLE IF NOT EXISTS categories (
        id SERIAL PRIMARY KEY NOT NULL,
        name VARCHAR(250) NOT NULL,
        parent_category_id INTEGER,
        FOREIGN KEY (parent_category_id) REFERENCES categories(id),
        CONSTRAINT unique_name_parent_category UNIQUE (name, parent_category_id)
    );

    CREATE TABLE IF NOT EXISTS resources(
        id SERIAL PRIMARY KEY NOT NULL,
        name VARCHAR(250) NOT NULL,
        amount NUMERIC(15, 2) NOT NULL,
        currency_code VARCHAR(3) NOT NULL, -- ISO 4217 code for currency (USD, EUR, BRL)
        category_id INTEGER NOT NULL,
        source_id INTEGER NOT NULL,
        FOREIGN KEY (category_id) REFERENCES categories(id),
        FOREIGN KEY (source_id) REFERENCES sources(id)
    );

"""

