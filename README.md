# Телеграм бот - планер

## Что делает данный бот?
&emsp; Данный бот (@ntlkay_bot) умеет ставить и выводить напоминания о записанных ему задачах

## Функциональность:
&emsp; Если человек пользуется ботом впервые, ему следует ввести команду "/start" в личные сообщения боту (@ntlkay_bot), и бот подскажет, как с ним работать дальше, а именно - выведет сообщение "Первый раз пользуетесь ботом? Напишите "/help" для вывода инструкции", что следует делать любому пользователю в случае если он забыл, как работает бот.

&emsp; Команда "/help" выводит инструкцию. Конкретно - сообщает пользователю, что ему необходимо написать "add_task" для того, чтобы добавить напоминание. Далее бот поэтапно спрашивает у пользователя сначала название задачи, которую он хочет поставить на напоминание, и время, когда бот должен отправить сообщение-напоминание ему в телеграм. Он сообщает о том, что напоминание было установлено.
 
&emsp; В установленное время бот отправит пользователю сообщение "Напоминание! Вам надо сделать следующее: (название задачи)".
 
 ![](images/screenshot1.png)


![](images/screenshot2.png)

&emsp; Кроме того, бот умеет обрабатывать ошибки, если пользователь ввёл дату и/или время, которые уже прошли, а также умеет рекомендовать использовать команду "/help" в случае, если пользователь не ввёл сообщение, подходящее по формату:

![](images/screenshot3.png)
 
## Инструкция по запуску бота на локальной машине:
```
git clone git@github.com:ntlkay/Telegram-bot.git
cd Telegram-bot
pip install -r requirements.txt
python3 main.py
```
Если на шаге клонирования репозитория потребуется пароль, - введите "1" (без кавычек)
