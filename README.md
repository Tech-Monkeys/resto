# Resto
An interactive chatbot for taking your orders build on top of Zulip, so as to return you the bill as well as the time taken to complete your order

## Usage

Run this bot as described in [here](https://zulipchat.com/api/running-bots#running-a-bot).


Use this bot with the following command

`@**resto bot** menu`


This will display the menu of the restaurant/cafe hosting the bot

Now, enter your order in the given syntax

```
<quantity_1> <item_1>
<quantity_2> <item_2>
.
.
<quantity_n> <item_n>
```

The bot displays the bill and gives a choice to either confirm or to update the order.

After the final confirmation, the bot gives out a final bill with the calculated time required to complete your order depending upon the previously stacked orders.

## Functions used in the code
* usage() --> Allow users to flag messages as being follow-up items
* handle_message() --> Handles user's messages.
* timer()--> calculates the time required to complete the order
* amount() --> calculates the billing amount
