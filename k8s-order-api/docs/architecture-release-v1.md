User / Tester
                         |
                         |
                  localhost:8080
                         |
                         v
                +----------------+
                |    Service     |
                | order-service  |
                |   ClusterIP    |
                +-------+--------+
                        |
                  label selector
                  app: order-api
                        |
            +-----------+-----------+
            |                       |
            v                       v
     +-------------+         +-------------+
     |    Pod 1    |         |    Pod 2    |
     |  order-api  |         |  order-api  |
     +-------------+         +-------------+
            \                       /
             \                     /
              +-------------------+
                       |
                 Deployment
                 replicas: 2
                       |
                ConfigMap/Secret
