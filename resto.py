from threading import Timer
import time
import datetime


class resto(object):
    '''
    A docstring documenting this bot.
    '''

    def __init__(self):
       self.order_completed = 0
       self.order_received = 0
       self.order = {}
       self.last_time = 0
       self.ref_time = 0

        

    def usage(self):
        return '''This bot helps you to get an approximate waiting time 
        and your bill in accordance to your order'''



    def handle_message(self, message, bot_handler):

        def timer():
            a=str((datetime.datetime.time(datetime.datetime.now())))
            r=a.split(":")
            entry_time = int(r[0])*60+int(r[1])
            if(self.ref_time == 0):
                self.ref_time = entry_time
                self.last_time = 10
                return 10
            timers = entry_time - self.ref_time
            if(self.last_time <= timers):
                self.last_time = timers + 10
                return 10
            self.last_time = self.last_time + 10
            return self.last_time - timers

        def amount(orderstring):
            menucard = {
                'patties':20,
                'bread_rolls':20,'brownie':40,'burger':30,'sandwich':25,'iced_tea':10,'lemon_tea':10,'cold_coffee':40,'maggi':25}
        
            strs= orderstring
            str1 = strs.split("\n")
            print(str1)
            price =0
            for element in str1:
                str2=element.split(" ")
                price = price + int(str2[0])*menucard[str2[1]]

            return price

        print(message)
        original_message = message['content']
        original_sender = message['sender_email']

        new_content = original_message.replace('@followup',
                                            'from %s:' % (original_sender,))

        if original_message == 'menu':
            response= '''  ****Menu****
                        patties          20
                        bread_rolls      20
                        brownie          40
                        burger            30
                        sandwich            25
                        iced_tea            10
                        lemon_tea          10
                        cold_coffee       40
                        maggi              25

                        Place Your Order:   '''
            bot_handler.send_reply(message, response)
            return

        elif original_message == 'update':
            response='Enter new Order'
            bot_handler.send_reply(message,response)
            return

        elif original_message == 'confirm':
            response='Your order is confirmed and it will take ' + str(timer()) +'minutes'
            self.order_received = self.order_received + 1
            bot_handler.send_reply(message,response)
            return

        else:
            response='You have ordered \n '+ original_message + '\n your bill is '+ str(amount(original_message))+' \n Do you want to update or confirm?'
            bot_handler.send_reply(message,response)
            return
            






handler_class = resto

