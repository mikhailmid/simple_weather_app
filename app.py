import asyncio
from time import sleep
from flask import Flask, render_template, request, flash
from pyowm.commons.exceptions import NotFoundError
from weather import get_current_weather, get_forecast

app = Flask(__name__)
app.secret_key = "123"


@app.route("/", methods=['GET'])
def main_page():
    city = request.args.get('city')
    if city:
        try:
            return render_template('index.html', current_weather=get_current_weather(city), forecasts=get_forecast(city))
        except NotFoundError:
            flash(f"Город \"{city}\" не найден")
    return render_template('index.html')

@app.route("/wait")
async def wait():
   await asyncio.sleep(5)
   return "Done"
    
    

if __name__ == "__main__":
    app.run(debug=True)
    