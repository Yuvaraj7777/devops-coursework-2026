# Exercise 6: Grafana Real-Time Monitoring

## Objective
Monitor a simulated quick-commerce delivery service using Python,
Prometheus, Grafana, and Jenkins.

## Files
- delivery_metrics.py: Generates delivery metrics.
- prometheus.yml: Prometheus scraping configuration.
- alert_rules.yml: Delivery alert rules.
- Dockerfile: Builds the Python metrics application.
- requirements.txt: Python dependencies.
- Jenkinsfile: CI pipeline.
- evidence/: Screenshots of genuine test results.

## Run locally

Install dependencies:

pip install -r requirements.txt

Start the metrics application:

python delivery_metrics.py

Open http://localhost:8000/metrics

## Monitoring services

Prometheus: http://localhost:9090
Grafana: http://localhost:3000
Jenkins: http://localhost:8080

Configure Grafana to use Prometheus as its data source.
Create panels for total deliveries, pending deliveries,
deliveries on the way, and average delivery time.

## Alerts

Prometheus evaluates the rules in alert_rules.yml.
Increase the pending delivery range in delivery_metrics.py
to test the high-pending-deliveries alert.

## Notes

Docker and Jenkins must be configured correctly for pipeline execution.
The Jenkins agent needs Docker CLI access and access to the Docker daemon.