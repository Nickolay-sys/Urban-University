from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = ''
bot = Bot(token = api)
dp = Dispatcher(bot, storage = MemoryStorage())

kb0 = ReplyKeyboardMarkup(resize_keyboard = True)
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Формулы расчёта')
button3 = KeyboardButton(text='Купить')
kb0.row(button1, button2, button3)



kb = InlineKeyboardMarkup(resize_keyboard = True)
kb_button1 = InlineKeyboardButton(text = 'Рассчитать', callback_data = 'calories')
kb_button2 = InlineKeyboardButton(text = 'Формулы расчёта', callback_data = 'formulas')
kb.row(kb_button1, kb_button2)



prod_kb = InlineKeyboardMarkup(resize_keyvoard = True)
prod_button1 = InlineKeyboardButton(text = 'Product1', callback_data = 'product_buying')
prod_button2 = InlineKeyboardButton(text = 'Product2', callback_data = 'product_buying')
prod_button3 = InlineKeyboardButton(text = 'Product3', callback_data = 'product_buying')
prod_button4 = InlineKeyboardButton(text = 'Product4', callback_data = 'product_buying')
prod_kb.add(prod_button1, prod_button2, prod_button3, prod_button4)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands = ['start'])
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup = kb0)


@dp.message_handler(text = ['Рассчитать'])
async def main_menu(message):
    await message.answer('Выберите опцию', replay_markup = kb)


@dp.message_handler(text = ['Купить'])
async def catalog(message):
    for i in range(1,5):
        await message.answer(f'Название: Product{i} |Описание: {i}|Цена: {i*100}')
        with open(f'prod_photo/{i}.jpg', 'rb') as img:
            await message.answer_photo(img)
    await message.answer('Выберите продукт для покупки:', reply_markup = prod_kb)
    
@dp.callback_query_handler(text = 'product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()
    

@dp.callback_query_handler(text = 'formulas')
async def get_formulas(call):
    await call.message.answer("для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;\n"
                              "для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161")
    await call.answer()


@dp.callback_query_handler(text = ['calories'])
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight = message.text)
    data = await state.get_data()
    calories = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age'])
    await message.answer(f"Ваша норма калорий {calories}")
    await state.finish()





@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)