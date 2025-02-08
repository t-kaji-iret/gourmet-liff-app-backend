CREATE TABLE IF NOT EXISTS restaurant_genre
(
    id        BIGINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    review_id BIGINT UNSIGNED  NOT NULL,
    genre_id  TINYINT UNSIGNED NOT NULL,
    UNIQUE (restaurant_id, genre_id)
);