CREATE TABLE IF NOT EXISTS image
(
    id            BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    review_id     BIGINT UNSIGNED NOT NULL,
    path          VARCHAR(255)    NOT NULL,
    thumbnail_flg BOOLEAN   DEFAULT FALSE,
    created_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX (review_id)
);