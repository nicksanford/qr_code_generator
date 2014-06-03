@manager.command
def deploy():
    if os.path.exists('.env'):
        print("Importing environment from .env...")
        for line in open(".env"):
            var = line.strip().split("=")
            if len(var) == 2:
                os.environ[ver[0]] = var[1]
