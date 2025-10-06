#!/bin/bash
set -e

KIBANA_URL="http://localhost:5601"
NDJSON="/usr/share/kibana/import/dashboard_imported_2.ndjson"

echo "Starting Kibana..."
/usr/local/bin/kibana-docker &

# Attendre que Kibana réponde
echo "Waiting for Kibana..."
until curl -s -o /dev/null -w "%{http_code}" "$KIBANA_URL/api/status" | grep -q "200"; do
  sleep 5
done

echo "Kibana is ready, importing dashboard..."
curl -s -X POST "$KIBANA_URL/api/saved_objects/_import?overwrite=true" \
  -H "kbn-xsrf: true" \
  --form file=@$NDJSON

echo "Import finished."
wait -n
