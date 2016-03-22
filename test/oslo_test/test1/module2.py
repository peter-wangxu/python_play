from __future__ import print_function
from oslo_config import cfg

opt_group = cfg.OptGroup(name='simple',
                         title='A Simple Example')
simple_opts = [
    cfg.BoolOpt('enable', default=False,
                help=('True enables, False disables'))
]
CONF = cfg.CONF
CONF.register_group(opt_group)
CONF.register_opts(simple_opts, opt_group)
