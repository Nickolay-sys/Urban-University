from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import crud_functions

api = "7649089484:AAGenO38ln9zKsiAxkrVcU3c9DEi14HL4KA"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    
class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()

kb0 = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text="Раcсчитать")
button2 = KeyboardButton(text="Купить")
button3 = KeyboardButton(text="Регистрация")
kb0.add(button1)
kb0.add(button2)
kb0.add(button3)

buy_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Product1', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product2', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product3', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product4', callback_data='product_buying')],
    ], resize_keyboard=True
    )

prod = crud_functions.get_all_products()

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    with open(f'prod_photo/1.jpg', 'rb') as img:
        await message.answer(f'Название: {prod[0][1]} | Описание: {prod[0][2]} | Цена:{prod[0][3]}')
        await message.answer_photo(img)
    with open(f'prod_photo/2.jpg', 'rb') as img:
        await message.answer(f'Название: {prod[1][1]} | Описание: {prod[1][2]} | Цена:{prod[1][3]}')
        await message.answer_photo(img)
    with open(f'prod_photo/3.jpg', 'rb') as img:
        await message.answer(f'Название: {prod[2][1]} | Описание: {prod[2][2]} | Цена:{prod[2][3]}')
        await message.answer_photo(img)
    with open(f'prod_photo/4.jpg', 'rb') as img:
        await message.answer(f'Название: {prod[3][1]} | Описание: {prod[3][2]} | Цена:{prod[3][3]}')
        await message.answer_photo(img)
    await message.answer(text="Выбирите продукт для покупки", reply_markup=buy_kb)
    
@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer(text="Вы успешно приобрели продукт!")

    
in_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="calories")],
        [InlineKeyboardButton(text="Формулы расчёта", callback_data='formulas')]
    ], resize_keyboard=True
    )
    
@dp.message_handler(text='Раcсчитать')
async def main_menu(message):
    await message.answer('Выберите опцию', reply_markup=in_kb)
    
@dp.callback_query_handler(text = 'formulas')
async def get_formulas(call):
    await call.message.answer("для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;\n"
                              "для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161")
    await call.answer()
    
@dp.message_handler(text="Регистрация")
async def sing_up(message):
    await message.answer('Введите имя ползователя (только латинский алфавит):')
    await RegistrationState.username.set()
    
@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if crud_functions.is_included(message.text):
        await message.answer("Пользователь  существует, введите другое имя")
        return
    await state.update_data(username=message.text)
    await message.answer("Введите свой email:")
    await RegistrationState.email.set()
    
@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()
    
@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    crud_functions.add_user(data['username'], data['email'], data['age'])
    await message.answer(f"Пользователь {data['username']} зарегистрирован")
    await state.finish()
  
@dp.callback_query_handler(text = ['calories'])
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    
@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.get_data(age = message.text)
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
    
@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup = kb0)
    
@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение')
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)