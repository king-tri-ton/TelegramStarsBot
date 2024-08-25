import telebot
from telebot import types
from config import TOKEN
from database import init_db, save_payment, get_photo_id
import os

bot = telebot.TeleBot(TOKEN)

# Инициализация базы данных
init_db()

# Функция для создания клавиатуры с кнопкой оплаты
def payment_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text="Оплатить 1 XTR", pay=True)
    keyboard.add(button)
    return keyboard

# Функция для создания клавиатуры с кнопкой "Купить изображение"
def start_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text="Купить изображение", callback_data="buy_image")
    keyboard.add(button)
    return keyboard

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(
        message.chat.id,
        "Добро пожаловать! Нажмите кнопку ниже, чтобы купить изображение.",
        reply_markup=start_keyboard()
    )

# Обработчик нажатия на кнопку "Купить изображение"
@bot.callback_query_handler(func=lambda call: call.data == "buy_image")
def handle_buy_image(call):
    prices = [types.LabeledPrice(label="XTR", amount=1)]  # 1 XTR
    bot.send_invoice(
        call.message.chat.id,
        title="Покупка изображения",
        description="Покупка изображения за 1 звезду!",
        invoice_payload="image_purchase_payload",
        provider_token="",
        currency="XTR",
        prices=prices,
        reply_markup=payment_keyboard()
    )

# Обработчик проверки платежа
@bot.pre_checkout_query_handler(func=lambda query: True)
def handle_pre_checkout_query(pre_checkout_query):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

# Обработчик успешного платежа
@bot.message_handler(content_types=['successful_payment'])
def handle_successful_payment(message):
    user_id = message.from_user.id
    payment_id = message.successful_payment.provider_payment_charge_id  # Или другой идентификатор платежа
    amount = message.successful_payment.total_amount
    currency = message.successful_payment.currency

    # Сначала отправляем сообщение о покупке
    bot.send_message(message.chat.id, "✅ Платеж принят, пожалуйста, ожидайте фото. Оно скоро придет!")
    
    # Сохраняем информацию о платеже в базу данных
    save_payment(user_id, payment_id, amount, currency)

    # После этого отправляем фото
    photo_path = 'img/img-X9ptcIuiOMICY0BUQukCpVYS.png'
    if os.path.exists(photo_path):
        with open(photo_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption="🥳Спасибо за вашу покупку!🤗")
    else:
        bot.send_message(message.chat.id, "Извините, изображение не найдено.")


# Обработчик команды /paysupport
@bot.message_handler(commands=['paysupport'])
def handle_pay_support(message):
    bot.send_message(
        message.chat.id,
        "Покупка изображения не подразумевает возврат средств. "
        "Если у вас есть вопросы, пожалуйста, свяжитесь с нами."
    )

# Запуск бота
bot.polling()
