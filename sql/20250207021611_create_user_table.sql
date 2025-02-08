CREATE TABLE IF NOT EXISTS user
(
    id           BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    line_user_id VARCHAR(255)     NOT NULL,
    name         VARCHAR(255)     NOT NULL,
    email        VARCHAR(255)     NOT NULL,
    tel          TINYINT UNSIGNED NOT NULL,
    created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX (line_user_id)
);