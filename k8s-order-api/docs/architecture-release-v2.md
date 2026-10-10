
                     Client
                       |
                       |
                order.localhost
                       |
                       v
                +-------------+
                |   Ingress   |
                | Controller  |
                +------+------+
                       |
                       v
                +-------------+
                |   Service   |
                | order-svc   |
                +------+------+
                       |
             +---------+---------+
             |                   |
             v                   v
       +-----------+       +-----------+
       |   Pod A   |       |   Pod B   |
       | order-api |       | order-api |
       +-----------+       +-----------+
             |                   |
             +---------+---------+
                       |
                    PVC/PV

            Deployment
                 |
       +---------+---------+
       |         |         |
   ConfigMap   Secret     HPA
