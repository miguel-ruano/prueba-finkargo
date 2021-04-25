from src import app as app_dir

app = app_dir.application(dev=False, config_path="environment/environment.docker.yml")
