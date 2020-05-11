#convert.py
#IPO or description

from graphics import *

def main():
    #create a window object
    win = GraphWin("Celcius converter", 400, 300)

    celsiusTempString = "Celcius Temperature:"
    fahrenheitTempString = "Fahrenheit Temperature:"

    Text(Point(150,50), celsiusTempString).draw(win)
    Text(Point(150, 250), fahrenheitTempString).draw(win)

    Rectangle(Point(125, 100), Point(275, 200)).draw(win)

    buttonText = Text(Point(200, 150), "Convert It")
    buttonText.draw(win)

    inputCelsiusField = Entry(Point(300, 50), 5)
    inputCelsiusField.setText("0.0")
    inputCelsiusField.draw(win)

    outputFahrField = Text(Point(300, 250), "")
    outputFahrField.draw(win)

    win.getMouse()

    celsiusTemperature = float(inputCelsiusField.getText())
    fahrenheit = 9.0/5.0 * celsiusTemperature + 32

    outputFahrField.setText(round(fahrenheit, 2))


    buttonText.setText("Quit")

    win.getMouse()



main()