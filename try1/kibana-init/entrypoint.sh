#!/bin/bash
set -e

KIBANA_URL="http://localhost:5601"

echo "Waiting for Kibana..."
until curl -s "$KIBANA_URL/api/status" | grep -q '"available"'; do
  sleep 5
done
echo "Kibana is up"

echo "Import dashboards..."
curl -X POST "$KIBANA_URL/api/saved_objects/_import?createNewCopies=true" \
  -H "kbn-xsrf: true" \
  --form file=@export_short.ndjson

echo "Create alerts..."
curl -X POST "$KIBANA_URL/api/alerting/rule" \
  -H "kbn-xsrf: true" \
  -H "Content-Type: application/json" \
  -d @alert_tachycardia.json

echo "Kibana initialization finished."
