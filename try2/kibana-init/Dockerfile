FROM docker.elastic.co/kibana/kibana:9.1.4

# On se place en root pour pouvoir copier des fichiers
USER root

# Copier fichiers de configuration et dashboard exporté
COPY dashboard_imported_2.ndjson /usr/share/kibana/import/dashboard_imported_2.ndjson
COPY entrypoint.sh /usr/local/bin/entrypoint.sh

# Donner droits d’exécution
RUN chmod +x /usr/local/bin/entrypoint.sh

# Revenir à l’utilisateur kibana (sécurité)
USER kibana

# Définir le script comme entrypoint
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
