# Imports, sets variables to starting values, and category dictionary to track the amount the user has spent for that category in that month. 
import turtle
import random
import math
user_input = "0"
fin_goal = "0"
remaining_balance = 0
goal_clicked = False
income_clicked = False
category = {
    "bills": 0,
    "dining": 0,
    "entertainment": 0,
    "grocery": 0,
    "health": 0,
    "savings": 0,
    "shopping": 0,
    "transportation": 0
}

# moneyWelcomeScreen Function - Create the money animation for the welcome screen, creates a 8x8 sqaure of the money.gif
# Parameters - None
# Returns - None
def moneyWelcomeScreen():
    money_count = 8
    for i in range(money_count):
        for l in range(money_count):
            money = turtle.Turtle()
            money.shape("imgs/money.gif")
            x = -180 + l * 50
            y = -120 + i * 50
            money.penup()
            money.goto(x, y)

# userInput Function - Gets the user_input variable and asks the user through turtle input the monthly income then changes the variable "income_clicked" that it was checked and writes the users income on the welcome screen
# Parameters - (x, y) Simple x and y axis points for when the user clicks the gif, must be used for the onlick feature to be used
# Returns - None
def userInput(x, y):
    global user_input
    t.penup()
    t.goto(170, -300)
    user_input = turtle.textinput("What is your monthly income?", "Monthly Income")
    t.write("$" + user_input, move=False, align="center", font=("Times New Roman", 20, "normal"))
    global income_clicked
    income_clicked = True
    checkNext()

# finInput Function - Gets the fin_goal variable and asks the user through turtle input the monthly income then changes the variable "goal_clicked" that it was checked and writes the users goal on the welcome screen
# Parameters - (x, y) Simple x and y axis points for when the user clicks the gif, must be used for the onlick feature to be used
# Returns - None
def finInput(x, y):
    global fin_goal
    t.penup()
    t.goto(-5, -300)
    fin_goal = turtle.textinput("What is your financial goal?", "Financial Goal")
    t.write("$" + fin_goal, move=False, align="center", font=("Times New Roman", 20, "normal"))
    global goal_clicked
    goal_clicked = True
    checkNext()

# checkNext Function - Checks if the goal_clicked and income_clicked is True meaning inputs neccessary given and then allows the screenTwo to be accessed
#Parameters - None
#Returns - None 
def checkNext():
    if goal_clicked and income_clicked:
        nextScreen.onclick(screenTwo)

# months_to_goal Function - Uses the remaining balance and the goal of the user and calculates the months to go to reach the goal
# Parameters - (remaining_balance, fin_goal) remaining_balance is the balance the user has which is updated each time, fin_goal is the goal the user has set at the beginning of the app
# Returns -  Months 
def months_to_goal(remaining_balance, fin_goal):
    months = math.ceil(fin_goal / remaining_balance)
    return months

# welcomeScreen Function - Create the welcome screen using the turtle graphics library
#Parameters - (t)
#Returns - None 
def welcomeScreen(t):
    width = 1370
    height = 710
    t.pensize(30)
    t.pencolor("gold")
    t.penup()
    t.goto(-width / 2 + 12.5, height / 2 - 12.5)
    t.pendown()
    for i in range(2):
        t.forward(width - 30)
        t.right(90)
        t.forward(height - 25)
        t.right(90)
    t.penup()
    t.goto(0, 280)
    t.color("black")
    t.write("Welcome to CashFlow Coach", move=False, align="center", font=("Times New Roman", 30, "bold"))
    t.goto(170, -220)
    t.write("Monthly Income", move=False, align="center", font=("Times New Roman", 15, "italic"))
    income = turtle.Turtle()
    income.shape("imgs/income.gif")
    income.penup()
    income.goto(170, -240)
    income.onclick(userInput)
    t.penup()
    t.goto(-5, -220)
    t.pendown()
    t.write("Financial Goal", move=False, align="center", font=("Times New Roman", 15, "italic"))
    goal = turtle.Turtle()
    goal.shape("imgs/goal.gif")
    goal.penup()
    goal.goto(-5, -240)
    goal.onclick(finInput)
    t.penup()
    t.goto(-185, -220)
    t.pendown()
    t.write("Start Tracking", move=False, align="center", font=("Times New Roman", 15, "italic"))
    global nextScreen
    nextScreen = turtle.Turtle()
    nextScreen.shape("imgs/next.gif")
    nextScreen.penup()
    nextScreen.goto(-185, -240)

# screenTwo Function - 
#Parameters - (x, y) Simple x and y axis points for when the user clicks the gif, must be used for the onlick feature to be used
#Returns - None 
def screenTwo(x, y):
    turtle.clearscreen()
    turtle.tracer(False)
    turtle.bgcolor("lightgreen")
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    width = 1370
    height = 710
    t.pensize(30)
    t.pencolor("gold")
    t.penup()
    t.goto(-width / 2 + 12.5, height / 2 - 12.5)
    t.pendown()
    for i in range(2):
        t.forward(width - 30)
        t.right(90)
        t.forward(height - 25)
        t.right(90)
    t.penup()
    t.goto(0, 280)
    t.color("black")
    t.write("Track Your Expenses", move=False, align="center", font=("Times New Roman", 30, "bold"))
    t.penup()
    t.goto(-180, 220)
    t.write("Transportation", move=False, align="center", font=("Times New Roman", 13, "normal"))
    transportation = turtle.Turtle()
    transportation.shape("imgs/transportation.gif")
    transportation.penup()
    transportation.goto(-180, 185)
    transportation.showturtle()
    t.penup()
    t.goto(0, 220)
    t.pendown()
    t.write("Groceries", move=False, align="center", font=("Times New Roman", 13, "normal"))
    grocery = turtle.Turtle()
    grocery.shape("imgs/grocery.gif")
    grocery.penup()
    grocery.goto(0, 185)
    grocery.showturtle()
    t.penup()
    t.goto(180, 220)
    t.pendown()
    t.write("Restaurants & Dining", move=False, align="center", font=("Times New Roman", 13, "normal"))
    dining = turtle.Turtle()
    dining.shape("imgs/dining.gif")
    dining.penup()
    dining.goto(180, 185)
    dining.showturtle()
    t.penup()
    t.goto(-180, 130)
    t.pendown()
    t.write("Entertainment", move=False, align="center", font=("Times New Roman", 13, "normal"))
    entertainment = turtle.Turtle()
    entertainment.shape("imgs/entertainment.gif")
    entertainment.penup()
    entertainment.goto(-180, 95)
    entertainment.showturtle()
    t.penup()
    t.goto(0, 130)
    t.pendown()
    t.write("Shopping", move=False, align="center", font=("Times New Roman", 13, "normal"))
    shopping = turtle.Turtle()
    shopping.shape("imgs/shopping.gif")
    shopping.penup()
    shopping.goto(0, 95)
    shopping.showturtle()
    t.penup()
    t.goto(180, 130)
    t.pendown()
    t.write("Health & Wellness", move=False, align="center", font=("Times New Roman", 13, "normal"))
    health = turtle.Turtle()
    health.shape("imgs/health.gif")
    health.penup()
    health.goto(180, 95)
    health.showturtle()
    t.penup()
    t.goto(-100, 30)
    t.pendown()
    t.write("Savings & Investments", move=False, align="center", font=("Times New Roman", 13, "normal"))
    savings = turtle.Turtle()
    savings.shape("imgs/savings.gif")
    savings.penup()
    savings.goto(-100, -10)
    savings.showturtle()
    t.penup()
    t.goto(100, 30)
    t.pendown()
    t.write("Bills & Subscriptions", move=False, align="center", font=("Times New Roman", 13, "normal"))
    bills = turtle.Turtle()
    bills.shape("imgs/bills.gif")
    bills.penup()
    bills.goto(100, -10)
    bills.showturtle()
    t.penup()
    t.goto(-10, -275)
    t.pendown()
    t.write("End Months Tracking", move=False, align="center", font=("Times New Roman", 15, "normal"))
    stop = turtle.Turtle()
    stop.shape("imgs/stop.gif")
    stop.penup()
    stop.goto(-10, -300)
    stop.showturtle()
    t.penup()
    t.pensize(5)
    t.pencolor("gold")
    t.goto(-683, -50)
    t.pendown()
    t.goto(683, -50)
    t.penup()
    t.goto(-10, -95)
    t.color("black")
    t.write("Current Expenses", move=False, align="center", font=("Times New Roman", 20, "bold"))
    t.goto(400, -145)
    t.color("black")
    t.write("Monthly Income: $" + user_input, move=False, align="center", font=("Times New Roman", 15, "normal"))
    t.goto(400, -195)
    t.color("black")
    t.write("Financial Goal: $" + fin_goal, move=False, align="center", font=("Times New Roman", 15, "normal"))
    turtle.update()
    turtle.tracer(True)

    # Event listeners to expense category turtles
    bills.onclick(handle_bills_click)
    dining.onclick(handle_dining_click)
    entertainment.onclick(handle_entertainment_click)
    grocery.onclick(handle_grocery_click)
    health.onclick(handle_health_click)
    savings.onclick(handle_savings_click)
    shopping.onclick(handle_shopping_click)
    transportation.onclick(handle_transportation_click)
    stop.onclick(endMonth)

# endMonth Function - This prompts the user how long it will take them to reach their financial goal
#Parameters - (x, y) Simple x and y axis points for when the user clicks the gif, must be used for the onlick feature to be used
#Returns - None 
def endMonth(x, y):
    monthsNeeded = months_to_goal(remaining_balance, int(fin_goal))
    t.goto(-10, -190)
    t.color("black")
    t.write(f"  Estimated {abs(monthsNeeded)} Months \nTo Reach Financial Goal", move=False, align="center", font=("Times New Roman", 15, "bold"))
    
# Handles click for all the expense categories
# Parameters - (x, y) Simple x and y axis points for when the user clicks the gif, must be used for the onlick feature to be used
# Returns - None
def handle_bills_click(x, y):
    global user_input, remaining_balance
    expense_category_clicked(x, y, t, "bills", user_input)
    user_input = str(remaining_balance)
    category["bills"] += 1

def handle_dining_click(x, y):
    global user_input, remaining_balance
    expense_category_clicked(x, y, t, "dining", user_input)
    user_input = remaining_balance
    category["dining"] += 1

def handle_entertainment_click(x, y):
    global user_input, remaining_balance
    expense_category_clicked(x, y, t, "entertainment", user_input)
    user_input = remaining_balance
    category["entertainment"] += 1

def handle_grocery_click(x, y):
    global user_input, remaining_balance
    expense_category_clicked(x, y, t, "grocery", user_input)
    user_input = remaining_balance
    category["grocery"] += 1

def handle_health_click(x, y):
    global user_input, remaining_balance
    expense_category_clicked(x, y, t, "health", user_input)
    user_input = remaining_balance
    category["health"] += 1

def handle_savings_click(x, y):
    global user_input, remaining_balance
    expense_category_clicked(x, y, t, "savings", user_input)
    user_input = remaining_balance
    category["savings"] += 1

def handle_shopping_click(x, y):
    global user_input, remaining_balance
    expense_category_clicked(x, y, t, "shopping", user_input)
    user_input = remaining_balance
    category["shopping"] += 1

def handle_transportation_click(x, y):
    global user_input, remaining_balance
    expense_category_clicked(x, y, t, "transportation", user_input)
    user_input = remaining_balance
    category["transportation"] += 1

# extract_data Function - Extract the data of average monthly expenses in the US
def extract_data():
    with open("data.txt", "r") as data_info:
        lines = data_info.readlines()
    data_dict = {}
    for line in lines:
        f_lines = line.strip().split(',')
        expense_category = f_lines[0]
        avg_expense = list(map(int, f_lines[1:]))
        data_dict[expense_category] = avg_expense
    return data_dict
    
# deduct_expense Function - Deducts avg expense cost from user income
# Parameters - (user_input, avg_expense_data, expense_category)
# Returns - None
def deduct_expense(user_input, avg_expense_data, expense_category):
    remaining_balance = 0  # Set a default value
    if user_input is not None:
        remaining_balance = int(user_input)
        if expense_category in avg_expense_data:
            avg_expense = avg_expense_data[expense_category]
            deduction = random.randint(avg_expense[0], avg_expense[1])
            remaining_balance -= deduction
    return remaining_balance

# expense_category_clicked Function - When an expense category is clicked, the user's balance is deducted from the avg of that expense
# Parameters (x, y, t, expense_category, user_input)
# Returns - None
def expense_category_clicked(x, y, t, expense_category, user_input):
    global remaining_balance
    remaining_balance = deduct_expense(user_input, avg_expense_data, expense_category)
    category[expense_category] += int(user_input) - remaining_balance
    turtle.tracer(False)
    t.clear()
    t.color("black")
    t.goto(400, -240)

    
    t.write("Remaining Balance: $" + str(remaining_balance), move=False, align="center", font=("Times New Roman", 15, "normal"))
    t.goto(-550, -100)
    
    # Write the updated balances for each expense category
    t.write(f"Transportation: ${category['transportation']}", move=False, align="center", font=("Times New Roman", 13, "normal"))
    t.goto(-550, -150)
    t.write(f"Entertainment: ${category['entertainment']}", move=False, align="center", font=("Times New Roman", 13, "normal"))
    t.goto(-550, -200)
    t.write(f"Savings & Investments: ${category['savings']}", move=False, align="center", font=("Times New Roman", 13, "normal"))
    t.goto(-550, -250)
    t.write(f"Groceries: ${category['grocery']}", move=False, align="center", font=("Times New Roman", 13, "normal"))
    t.goto(-550, -300)
    t.write(f"Shopping: ${category['shopping']}", move=False, align="center", font=("Times New Roman", 13, "normal"))
    t.goto(-325, -150)
    t.write(f"Restaurants & Dining: ${category['dining']}", move=False, align="center", font=("Times New Roman", 13, "normal"))
    t.goto(-325, -200)
    t.write(f"Health & Wellness: ${category['health']}", move=False, align="center", font=("Times New Roman", 13, "normal"))
    t.goto(-325, -250)
    t.write(f"Bills & Subscriptions: ${category['bills']}", move=False, align="center", font=("Times New Roman", 13, "normal"))

    # Display a warning message if the remaining balance is too low
    if remaining_balance <= 100:
        t.goto(425, 275)
        t.color("red")
        t.write("                     Warning:\n You are spending too much money!", move=False, align="center", font=("Times New Roman", 15, "bold"))

# User console inputs & function calls
# Set up screen & add all images as shapes 
s = turtle.Screen()
s.setup(width=1370, height=710)
s.bgcolor("lightgreen")
turtle.hideturtle()
turtle.tracer(False)  # Disable animation during setup
turtle.addshape("imgs/money.gif")
turtle.addshape("imgs/next.gif")
turtle.addshape("imgs/transportation.gif")
turtle.addshape("imgs/grocery.gif")
turtle.addshape("imgs/dining.gif")
turtle.addshape("imgs/entertainment.gif")
turtle.addshape("imgs/shopping.gif")
turtle.addshape("imgs/health.gif")
turtle.addshape("imgs/savings.gif")
turtle.addshape("imgs/bills.gif")
turtle.addshape("imgs/income.gif")
turtle.addshape("imgs/goal.gif")
turtle.addshape("imgs/stop.gif")
t = turtle.Turtle()
t.hideturtle()
welcomeScreen(t)
turtle.tracer(True)
moneyWelcomeScreen()
avg_expense_data = extract_data()
turtle.mainloop()