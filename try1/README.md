# Requirements

Make sure your ports are free:
* 9200 (ElasticSearch)
* 5044 (Logstash)
* 5601 (Kibana)

# Getting started

Get into the folder with `docker-compose.yml`.
```
sudo docker compose up -d
```
It may take about 1min to get every services running.

Open Kibana in browser using `http://localhost:5601`

## Dashboard

Create your own dashboard in Kibana:
1. Go into the left menu.
2. Click `Management > Stack Management`
3. Click `Kibana > Data Views`
4. Click `Create data views`

5. Click `Analytics > Discover`

5. Click `Analytics > Visualize Library`
6. Click `Create new visualization`
7. Recommend choosing `Lens`

8. When done `Save` into your favorite Dashboard.

# Security issues

- Communication of data from sensor to Logstash is not encrypted.
- ElasticSearch security is now deactivated.

# Other issues

- Real-Time data acquisition does not seem to be real-time enough: lag for data to appear in dashboard.