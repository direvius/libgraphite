A Python library for querying metrics from Graphite using its URL API into Pandas DataFrames. Use like this:

```
df = lg.Query(graphite) \
        .target('aliasByMetric(five_sec.my.favourite.metric)') \
        .pfrom('-3d') \
        .puntil('-1d') \
        .execute()
```