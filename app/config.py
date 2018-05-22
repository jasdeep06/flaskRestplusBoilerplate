
class Config:
    DEBUG=False



class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    postgres = {
        'user': 'postgres',
        'pw': 'biology12',
        'db': 'apitrial',
        'host': 'localhost',
        'port': '5432',
    }
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % postgres


config_by_name=dict(dev=DevelopmentConfig)