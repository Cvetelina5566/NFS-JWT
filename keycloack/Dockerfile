# Използваме официалния образ на Keycloak
FROM jboss/keycloak:latest

# Задаваме административни потребител и парола (ако не ги зададете чрез docker-compose.yml)
ENV KEYCLOAK_USER=admin
ENV KEYCLOAK_PASSWORD=admin

# Копираме предварително дефинирани конфигурации, ако са налични (опционално)
COPY realms/ /opt/keycloak/data/import/

# Включваме автоматичен импорт на realm-и при стартиране
ENV KEYCLOAK_IMPORT=/opt/keycloak/data/import/realm.json

# Стартиране на Keycloak
ENTRYPOINT ["/opt/jboss/tools/docker-entrypoint.sh"]

# Задаваме порта за Keycloak
EXPOSE 8080
