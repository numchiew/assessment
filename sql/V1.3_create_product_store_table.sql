CREATE TABLE db_name.product_display (
    product_id BIGINT NOT NULL REFERENCES db_name.product(id) ON UPDATE CASCADE ON DELETE CASCADE,
    store_id BIGINT NOT NULL REFERENCES db_name.store(id) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT product_store_pk PRIMARY KEY (product_id, store_id)
);