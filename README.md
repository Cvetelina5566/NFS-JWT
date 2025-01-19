# File Management System

## Структура на проекта

- `docker-compose.yml`: Основен файл за конфигуриране на Docker услуги.
- `app/`: Приложението за управление на файлове.
- `keycloak/`: Docker конфигурация за Keycloak.
- `nfs/`: Docker конфигурация за NFS сървър.

## Стартиране на проекта

1. Изтеглете репозиториума:

    ```bash
    git clone https://github.com/Cvetelina5566/NFS-JWT.git
    cd file-management
    ```

2. Стартирайте всички услуги:

    ```bash
    docker-compose up --build
    ```

3. Приложението ще бъде достъпно на [http://localhost:5000](http://localhost:5000).

4. Keycloak ще бъде достъпен на [http://localhost:8080](http://localhost:8080).
