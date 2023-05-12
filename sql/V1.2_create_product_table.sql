CREATE SEQUENCE db_name.product_id_sequence;

CREATE TABLE db_name.product (
    id BIGINT NOT NULL DEFAULT nextval('db_name.product_id_sequence'),
    user_id BIGINT NOT NULL,
    title VARCHAR(255) NOT NULL,
    description VARCHAR(255) NOT NULL,
    price NUMERIC(10, 3) NOT NULL,
    available_date TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    quantity INTEGER NOT NULL CHECK (price >= 0),
    image_uri VARCHAR(255) NOT NULL,
    is_special BOOLEAN NOT NULL,
    category VARCHAR(255) NOT NULL,
    tags JSON,
    created_time TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    modified_time TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_user FOREIGN KEY(user_id) REFERENCES db_name.user(id)
);
