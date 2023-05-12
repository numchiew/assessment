CREATE SEQUENCE db_name.store_id_sequence;
CREATE TYPE db_name.store_type AS ENUM ('MicroStore', 'StoreFront');

CREATE TABLE db_name.store (
    id BIGINT NOT NULL DEFAULT nextval('db_name.store_id_sequence'),
    user_id BIGINT NOT NULL,
    store_name VARCHAR(255) NOT NULL,
    description VARCHAR(255) NOT NULL,
    contact_information VARCHAR(255) NOT NULL,
    store_type db_name.store_type NOT NULL,
    created_time TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    modified_time TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_user FOREIGN KEY(user_id) REFERENCES db_name.user(id)
);