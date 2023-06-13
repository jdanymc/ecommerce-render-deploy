from datetime import timedelta
class Config:
    #SQLALCHEMY_DATABASE_URI = 'mysql://root:123456.a@localhost/db_shop_g20'
    SQLALCHEMY_DATABASE_URI = 'postgresql://db_shop_g20_user:pE8WvuG1h4fJEmLvISyAbXADVLmAN7JD@dpg-ci3s37liuie031lrs1b0-a.ohio-postgres.render.com/db_shop_g20'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'secret'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)