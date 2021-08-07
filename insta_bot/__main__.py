"""основной модуль инстаграм бота"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pathlib import Path
from insta_bot import insta_main_func
from time import sleep
from bs4 import BeautifulSoup


if __name__ == '__main__':
    """все запуски будут происходить здесь"""
    # настраваем драйвера
    options = Options()
    options.add_argument('__headless')
    options.add_argument("--start-maximized")

    # определяю разные уровни для засыпания
    # ввел эти значения, чтобы иметь возможность одним изменением менять весь скорость программы
    # для одних компов может понадобиться для работы одна, для других другая скорость
    l = 10 # low
    m = 5 # medium
    f = 3 # fast
    sf = 1 # super fast

    # указываю путь до хромиума. Path.cwd() возвращает путь к проекту
    path_to_chromium = Path.cwd() / 'resources' / 'chrome' / 'chrome-win' / 'chrome.exe'
    options.binary_location = f'{path_to_chromium}'
    # указываю путь до хромдрайвера
    path_to_chromedriver = Path.cwd() / 'resources' / 'chromedriver' / 'chromedriver.exe'

    # запускаем драйвер
    driver = webdriver.Chrome(f'{path_to_chromedriver}', options=options)

    # заходим в сайт
    driver.get('https://www.instagram.com/')

    # вводим данные и входим в аккаунт
    insta_main_func.write_log_pass_submit(driver)

    # спим 5 с, чтобы программа работала корректно.
    # иначе следующий поиск для нажатия кнопки будет происходить на этой странице
    sleep(m)

    # инста запрашивает сохранить данные. нажимаем не сейчас
    insta_main_func.not_now_save_my_date(driver)

    # спим 1 с, чтобы программа работала корректно.
    # иначе следующий поиск для нажатия кнопки будет происходить на этой странице
    sleep(sf)

    # инста запрашивает включить уведомление. нажимаем не сейчас
    insta_main_func.not_now_on_notif(driver)

    # спим 1 с, чтобы программа работала корректно.
    # иначе следующий поиск для нажатия кнопки будет происходить на этой странице
    sleep(sf)

    # вводим слово для поиска и непосредственно поиск
    # ВОТ ЗДЕСЬ ЧАСТО ПАДАЕТ БОТ. НАДО СЛОВИТЬ ОШИБКУ
    # КАЖЕТСЯ ЗДЕСЬ НАДО ИМЕННО КЛИКАТЬ, А НЕ ENTER НАЖИМАТЬ. ИНАЧЕ ОНО МОЖЕТ ПАДАТЬ ПРИ ЗАКРЫТОМ ОКНЕ.
    insta_main_func.write_word_in_search(driver)

    # спим 5 с, чтобы программа работала корректно.
    # иначе следующий поиск для нажатия кнопки будет происходить на этой странице
    sleep(m)

    # кликаем по результату поиска
    insta_main_func.click_on_result_from_search(driver)

    # спим 1 с, чтобы программа работала корректно.
    # иначе следующий поиск для нажатия кнопки будет происходить на этой странице
    sleep(sf)

    # кликаем по кнопке нравится, чтобы получать список лаикавших
    insta_main_func.click_who_liked(driver)

    # поробуем сон, чтобы все норм загрузилось перед парсингом
    sleep(5)

    # получаю html код
    html = driver.page_source

    # в списке like_people_list буду сохранять имена лаикнувших пользователей
    like_people_list = []
    # настраиваю BeautifulSoup
    soup = BeautifulSoup(html, features="html.parser")
    for tag in soup.find_all('a', href=True):
        # получаю каждого пользователя по ключу 'href'
        like_people_list.append(tag['href'])
    print(like_people_list)
    # делаем реверс и ищем элемент(который стоит выше href с именами пользователей) с конца
    like_people_reverse_list = like_people_list[::-1]
    find_not_use_href_index_reverse = like_people_reverse_list.index('/p/CSHaur0jvqZ/')

    # находим нормальный индекс(без реверса) элемента
    normal_index = len(like_people_list) - (find_not_use_href_index_reverse + 1)


    # ЗДЕСЬ НАДО ЗАПРИНТОВАТЬ like_people_list ПРАВИЛЬНО ЛИ ОНО УКАЗАНО

    # удаляем все ненужные ссылки
    # ВСЕ ЕЩЕ НЕ ПРАВИЛЬНО РАБОТАЕТ. НАДО УЗНАТЬ, КАК РАБОТАЕТ ПОП.
    while normal_index > 0:
        like_people_list.pop()
        normal_index -= 1




    print(like_people_list)
    # driver.quit()
