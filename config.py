from environs import Env

env = Env()
env.read_env('.env')

WEATHER_API_TOKEN = env.str("OWM_TOKEN")