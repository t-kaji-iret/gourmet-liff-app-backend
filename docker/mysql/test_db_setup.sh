mysql -u root --password=password -e "
CREATE DATABASE IF NOT EXISTS \`test-gourmet-app\`;
CREATE USER 'root'@'localhost' IDENTIFIED WITH caching_sha2_password BY 'password';
FLUSH PRIVILEGES;
"

for file in docker-entrypoint-initdb.d/*.sql; do
  mysql -u root --password=password test-gourmet-app < "$file"
done