# odoo-orm-cache

## Dependencies
`odoo-orm-cache` uses [`redis`](https://redis.io/) to store cache into redis server. You will need to install it.


## Compatibility
This module is compatible with **Odoo 11** and **Python 3**. For older versions, you can refer to the original source code (see credits below).

## Configuration
In order to use `odoo-orm-cahe` you will need to edit etc/odoo/odoo.conf file:
* modify the master odoo.conf file:
```
    ormcache_redis_url=redis://@redis-ip:6379/0 
    ormcache_redis_expire=604800
```

## Additional Information and Credits
This code is [custom from this repo](https://github.com/openliu/Odoo-Cluster) it using odoo 10 and this repo use for Odoo v11.0 and using it as modular.

