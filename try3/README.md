This try is to load pre-configured dashboard and alert in Kibana, with RBAC.

# Requirements

Make sure your ports are free:
* 9200 (ElasticSearch)
* 5044 (Logstash)
* 5601 (Kibana)

Make sure you can run `docker` and `docker-compose`:
```bash
sudo apt-get update && sudo apt-get install docker-compose docker -y
```

# Getting started

Get into the folder with `docker-compose.yml`.
```bash
sudo docker compose up -d --build
```
It may take about 1min to get every services running.

Open Kibana in browser using `http://localhost:5601/app/home`

## Dashboard

Create your own dashboard in Kibana:

1. Go into the left menu.
---
2. Click `Management > Stack Management`
3. Click `Kibana > Data Views`
4. Click `Create data views`

1. Go back to the left menu.
5. Click `Analytics > Discover`
---
1. Go back to the left menu.
5. Click `Analytics > Visualize Library`
6. Click `Create new visualization`
7. Recommend choosing `Lens`

8. When done `Save` into your favorite Dashboard.
9. To change time span and set a refresh time interval, click onto the calendar icon, next to the refresh data button.

## Alerts

To create alerts on Kibana, please follow the instructions:

1. Go into the left menu.
2. Click `Management > Stack Management`
3. Click `Rules`
4. Click `Create rule`
5. Choose `Elasticsearch query` or `Custom Threshold`
6. Set up your rule. As an example, you can set up an alarm that triggers every time an athlete's heart rate is above 175 bpm. In order to do that:
    - Choose `Custom Threshold`
    - Choose the data view associated to `medical-signals`
    - Set aggregation A to `MAX heart_rate`
    - Set equation and threshold to `EQUATION A` and `IS ABOVE 175`
    - Set time window to be `FOR THE LAST 5 seconds`
    - Set alert's check frequency to `Every 5 seconds`
    - Save with the name `Heart rate > 175`

You are ready to go.
You can see alerts in `Observability > Alerts`, and choose to show `rule 'Heart rate > 175'`.

To link to a Kibana log output:
1. Create a connector in `Management > Stack Management > Connectors`, with name `Heart rate alert logs` for example.
2. Go to your rule (e.g. `Management > Stack Management > Rules`) and edit it.
3. Click `Add action` and select the connector you just created.

To add a visualization onto the Dashboard:
1. Click on `Add panel`
2. Choose `Visualizations > Alerts`
3. Choose `Solution: Observability`
You got it.

## DASHBOARD and ALERT already imported

#### First step: Activate alert

1. Go to the menu on the left.
2. Go to `Observability > Alerts`
3. `Manage Rules`
4. Enable rule `Heart Rate > 175`

#### Second step: Get to the preset dashboard

1. Go to the menu on the left.
2. Go to `Analytics > Dashboards`
3. We recommand setting `Last 1 minute` and refresh every `1 second`, in the calendar icon.

Unfortunately, the auto-refresh does not work as intended when the table of alerts is there.
So you have to refresh it manually by clicking the refresh button next to the calendar icon.

# Security issues

- Communication of data from sensor to Logstash is not encrypted.
- ElasticSearch security is now deactivated.

# Other issues

- Real-Time data acquisition does not seem to be real-time enough: lag for data to appear in dashboard.
