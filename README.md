# SolrWatch

SolrWatch is a Solr monitoring tool, which can track important metrics about Solr performance and visualize it. 

## Metrics

Currently it tracks the following metrics:

### General

* Total number of documents
* Document growth rate
* Document deletion rate
* JVM heap usage
* Segment count, segments generation rate

### Query Handlers

Query handlers handle incoming requests. User can define multiple query handler. For each defined handler, the following metrics are tracked:

* Throughput (Requests/minute)
* Error rate (Errors/minute)
* Timeout rate (Timeouts/minute)
* Response time (Avg response time/minute)

### Update Handlers

Update handlers handle indexinn requests. For each defined update handler, the following metrics are tracked:

* Commit rate (commits/minute)
* Autocommit rate (autocommits/minute)
* Indexing rate (Documents indexed/minute)
* Error rate (Errors/minute)
* Optimize rate (Optimizes/minute)
* Total no. of transaction logs
* Total size of transaction logs
