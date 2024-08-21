import os

class Config:
    # Secret key for session management and other security features
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # SQLAlchemy settings for PostgreSQL database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://username:password@localhost/ticket_remittance_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Static files settings (optional, Flask serves static files by default)
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

    # Flask-RESTPlus settings (if applicable)
    RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
    RESTPLUS_VALIDATE = True
    RESTPLUS_MASK_SWAGGER = False
    ERROR_404_HELP = False

    # Security and authentication settings (e.g., for Flask-Login or other tools)
    # Example (if using Flask-Login):
    # LOGIN_VIEW = 'auth.login'

    # Email settings (if your app sends emails, e.g., for password resets)
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.example.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') or True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER') or 'noreply@example.com'

    # Additional configurations for scalability or deployment
    DEBUG = os.environ.get('DEBUG') or False
    TESTING = os.environ.get('TESTING') or False

    # AWS or other cloud services settings (if applicable)
    # Example (for AWS S3):
    # S3_BUCKET = os.environ.get('S3_BUCKET')
    # S3_ACCESS_KEY = os.environ.get('S3_ACCESS_KEY')
    # S3_SECRET_KEY = os.environ.get('S3_SECRET_KEY')

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # Use an in-memory database for testing

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    # Use the environment variable or a secure configuration management tool for production DB URI
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

# Dictionary to easily switch between different configurations
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
