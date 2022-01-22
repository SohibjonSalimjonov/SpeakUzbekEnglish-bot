import logging
from aiogram import Bot, Dispatcher, executor, types


from UzEnBot import UzEn
from googletrans import Translator
translator=Translator()

API_TOKEN = '5214427222:AAGAj-hC3nYGYeU8xKeMUll7y1LbuqxsjXY'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Assalomu alaykum. UzbekEnglish botiga xush kelibsiz!")
@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.answer('Bu bot ingliz tilidagi so\'zlarni ma\'nolarini va audiosini chiqarib beradi.\nBundan tashqari kiritgan matnlaringizni o\'zbek tilidan ingliz tiliga tarjima qilib beradi.')

@dp.message_handler()
async def echo(message: types.Message):

    lang=translator.detect(message.text).lang
    if len(message.text.split())>2:
        dest='uz' if lang=='en' else 'en'
        await message.answer(translator.translate(message.text,dest).text)
    else:
        if lang=='en':
            soz=message.text
        else:
            soz=translator.translate(message.text, dest='en').text
    look=UzEn(soz)
    if look:
        await message.answer(f"\n{look['definitions']}")
        if look.get('audio'):
            await message.answer_voice(look['audio'])
    else:
        await message.answer('Bunday so\'z topilmadi!')




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)