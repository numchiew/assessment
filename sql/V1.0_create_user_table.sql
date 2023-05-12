CREATE SEQUENCE db_name.user_id_sequence;

CREATE TABLE db_name.user (
    id BIGINT NOT NULL DEFAULT nextval('db_name.user_id_sequence'),
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    dob TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    address VARCHAR(255) NOT NULL,
    contact_number VARCHAR(255) NOT NULL,
    created_time TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    modified_time TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    PRIMARY KEY (id)
);