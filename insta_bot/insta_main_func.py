"""модуль с основными функциями для инстаграм бота"""
from . import keys
import keyboard
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def write_log_pass_submit(driver):
    """функция, для ввода имени пользователя и логина"""
    # находим поле для ввода имени пользователя
    input_username = WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.NAME, 'username')))
    # вводим данные
    input_username.send_keys(keys.my_username)
    # находим поле для ввода пароля
    input_pass = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, 'password')))
    # вводим пароль
    input_pass.send_keys(keys.my_pass)
    # находим кнопку вход, для подтверждения и входа
    button_submit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.Igw0E.IwRSH.eGOV_._4EzTm')))
    # кликаем по кнопке для подтвержения и входа
    button_submit.click()


def not_now_save_my_date(driver):
    """фцнкция для нажатия на кнопку не сейчас, при запрашивании сохранения данных при входе"""
    button_not_now_save_my_date = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.sqdOP.yWX7d.y3zKF')))
    button_not_now_save_my_date.click()


def not_now_on_notif(driver):
    """функция для нажатия на кнопку не сейчас, при запрашивании включить уведомления"""
    button_not_now_on_notif = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.aOOlW.HoLwm')))
    button_not_now_on_notif.click()


def write_word_in_search(driver):
    """функция для ввода хэштега или любого слова для поиска и непосредственно поиска"""
    input_word_for_search = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.XTCLo.x3qfX')))
    input_word_for_search.send_keys('#python')
    # нажать нужно два раза. при первом нажатии выбирается вариант
    # для поиска(там будет выпадающий список для поиска. во втором нажатии уже непосрдственно поиск

    # берем небольшую паузу перед нажатием enter, чтобы бот не падал
    sleep(1)
    keyboard.send('enter')
    # между нажатиями кнопок словим паузу, чтобы не вызывались ненужные баги
    sleep(1)
    keyboard.send('enter')


def click_on_result_from_search(driver):
    """функция для нажатия на результат поиска(фото, видео)"""
    resul_from_search = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '._9AhH0')))
    resul_from_search.click()


def click_who_liked(driver):
    """функция для нажатия на кнопку 'нравится' чтобы получать список лаикавших"""
    button_who_liked = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.zV_Nj')))
    button_who_liked.click()