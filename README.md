## Development:


    docker build -t mail-exporter .

    docker run -it -p 5000:5000 -e EMAIL_ACCOUNTS=imap.host.first:email@email.com:password1,imap.host.second:email2@email.com:password2 email-exporter


Open:

    http://localhost:5000/metrics

# Running

Start container somewhere

## Prometheus:

```
scrape_configs:
  - job_name: 'email-exporter'
    static_configs:
      - targets: ['localhost:5000']
```


## Grafana:

Visualize in Grafana:

- Setup a Prometheus data source in Grafana.
- Create a new dashboard in Grafana.
- Add a panel that queries email_unread_count.

# Warnings

Take care of your secrets. The solution is not production ready. Host it in private network just to be sure.


