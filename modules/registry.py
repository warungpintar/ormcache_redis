# -*- coding: utf-8 -*-
from odoo.tools import (assertion_report, config, existing_tables,
                        lazy_classproperty, lazy_property, table_exists,
                        topological_sort, OrderedSet)
import logging
import odoo
from ..tools.RedisLRU import RedisLRU
import redis
from odoo.modules.registry import Registry


_logger = logging.getLogger(__name__)


# class Registry_inherit(Mapping):
#
@lazy_property
def cache(self):
    r=redis.StrictRedis.from_url(odoo.tools.config['ormcache_redis_url'])
    db_name = self.db_name
    return RedisLRU(r,db_name)

if odoo.tools.config.get('ormcache_redis_url'):
    Registry.cache = cache
