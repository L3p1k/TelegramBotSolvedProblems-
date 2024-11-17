from telebot import TeleBot, types

bot = TeleBot('(свой API код бота)')



@bot.message_handler(commands=['start'])
def start(message: types.Message):
    bot.send_message(message.chat.id, 'Пиши /help чтобы узнать всё подробнее о боте, для чего он нужен и как им пользоваться')
    

@bot.message_handler(commands=['help'])
def help(message: types.Message):
    bot.send_message(message.chat.id, 'Привет, я создан для улучшения жизни в целом и намерен рассказать об экологических проблемах и их решений. Пиши /find чтобы найти проблему и её решение)   Если ничего не понятно — /what')
    
    
@bot.message_handler(commands=['find'])
def find(message: types.Message):
    bot.send_message(message.chat.id, 'Узнать о рандомной проблеме экологии — /random;')
    
    
@bot.message_handler(commands=['what'])
def what(message: types.Message):
    bot.send_message(message.chat.id, 'Пока что я создан только для решения проблем экологии, но в будущем уже возможно и для других проблем. Каким образом я могу сделать жизнь лучше? Во первых ты сам должен захотеть изменить мир в хорошую сторону, хотябы чуть-чуть. Во вторых я говорю проблемы, которые сейчас актуальны и просто следуй инструкции, так как когда ты начнёшь двигаться и действовать в ближайшее время, то возможно конца света никогда не будет. В третьих это маленькая часть проекта "Венера", ты можешь посмотреь что такое проект "Венера", здесь более подробно о проекте — https://youtu.be/YvRHN838N3A?si=4dzWhPUC5gxhc8Ve. Ну и заключительно хочу сказать будущее рядом!))')
    
    
@bot.message_handler(commands=['random'])
def random(message:types.Message):
