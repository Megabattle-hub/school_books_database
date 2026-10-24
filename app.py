import flask as fl
from view import render_page

# программа для запуска в браузере
app = fl.Flask(__name__)
@app.route("/")



def index():

    # задаём тестовый список книг
    books = [
        {"name": "Название1", "author": "Автор1", "ISBN": "1"},
        {"name": "Название2", "author": "Автор2", "ISBN": "2"},
        {"name": "Название3", "author": "Автор3", "ISBN": "3"},
        {"name": "Название4", "author": "Автор4", "ISBN": "4"},
        {"name": "Название5", "author": "Автор5", "ISBN": "5"}
    ]

    # вызываем создание страницы
    html_page = render_page(books)
    return html_page

# запуск самой программы
if __name__ == "__main__":
    app.run(debug=True)