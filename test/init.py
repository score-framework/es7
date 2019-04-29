import os
from score.init import init
import configparser


config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__),
                         '..', 'pytest.ini'))
valid_host = config['es7']['valid_host']


def test_defaults():
    score = init({
        'score.init': {'modules': 'score.es7'},
        'es7': {'args.hosts': valid_host},
    })
    assert score.es7.client


def test_destroy():
    score = init({
        'score.init': {'modules': 'score.es7'},
        'es7': {'args.hosts': valid_host},
    })
    score.es7.destroy()


def test_create():
    score = init({
        'score.init': {'modules': 'score.es7'},
        'es7': {'args.hosts': valid_host},
    })
    score.es7.create()
