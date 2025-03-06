mysql -u root --password=password -e "
CREATE DATABASE IF NOT EXISTS \`test-gourmet-app\`;
CREATE USER 'root'@'127.0.0.1' IDENTIFIED WITH caching_sha2_password BY 'password';
FLUSH PRIVILEGES;
"