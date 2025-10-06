FROM alpine:3.19

RUN apk add --no-cache curl bash jq

WORKDIR /init

COPY entrypoint.sh .
COPY export_short.ndjson .
COPY alert_tachycardia.json .

RUN chmod +x entrypoint.sh
CMD ["./entrypoint.sh"]
