from datetime import datetime
from flask import Flask

app = Flask(__name__)

@app.route('/')
def time():
    current_time = datetime.now().strftime('%d.%m.%Y %H:%M')
    html = f'''
    <h2>Текущая дата и время</h2>
    <p>{current_time}</p>
    '''
    return html

if __name__ == __name__:
    app.run()