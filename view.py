# страница
import pyhtml as p

# создание страницы
def render_page(books):

    # создание карточек книг
    decks = []
    for deck in books:
        decks.append(p.div(deck["name"], deck["author"], deck["ISBN"]))

    # создание самой страницы
    page = p.html(

        # импорт стилей
        p.head(p.link( rel="stylesheet", href="static\style.css")),

        # создание тела страницы
        p.body(

            # создание шапки
            p.nav(
                p.div(class_ = "navbar")(
                    p.img(src = "https://ir.ozone.ru/s3/cms/e3/tc1/wc200/group_2087330924.png"),
                    p.h1("Школьные учебники")
                )
            ),

            # создание списка
            p.div(decks)
        )
    )

    return str(page)