CREATE TABLE IF NOT EXISTS review
(
    id              BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    user_id         BIGINT UNSIGNED NOT NULL,
    restaurant_name VARCHAR(255)    NOT NULL,
    nearest_station VARCHAR(255)    NOT NULL,
    comment         VARCHAR(255)    NOT NULL,
    url             VARCHAR(255),
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (user_id)
);