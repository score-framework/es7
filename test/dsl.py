import os
from score.init import init
import configparser
from elasticsearch_dsl import Search
from score.es7.dsl import DslExtension


config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__),
                         '..', 'pytest.ini'))
host = config['es7']['valid_host']


def test_defaults():
    score = init({
        'score.init': {'modules': ['score.es7', 'score.ctx']},
        'es7': {'args.hosts': host},
    })
    with score.ctx.Context() as ctx:
        assert isinstance(ctx.es, DslExtension)
        assert isinstance(ctx.es.dsl.search(), Search)
