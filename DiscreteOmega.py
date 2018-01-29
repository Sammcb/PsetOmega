import random
import sys
import multiprocessing
from time import sleep
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class GameWindow(QWidget):
	
	def __init__(self):
		super().__init__()

		self.questions = ["The left door is the good door.", "The left door is the bad door.", "The right door is the good door.", "The right door is the bad door."]

		self.operators = ["AND", "OR", "XOR", "IMPLIES", "IFF", "NAND"]
		self.values = ["T","F"]
		self.booleanValues = {"T":True, "F":False}
		self.operatorValues = {"AND": lambda a,b: a and b, "OR": lambda a,b: a or b, "XOR": lambda a,b: a != b, "IMPLIES": lambda a,b: ((not a) or b), "IFF": lambda a,b: a == b, "NAND": lambda a,b: not(a and b)}

		self.setWindowTitle("Two Doors")
		self.setGeometry(100, 100, 720, 405)
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

		oImage = QImage("Slide02.png")
		palette = QPalette()
		palette.setBrush(10, QBrush(oImage))
		self.setPalette(palette)
		self.show()

		timer = QTimer(self)
		timer.timeout.connect(self.secondImage)
		timer.setSingleShot(True)
		timer.start(3000)

	def secondImage(self):
		oImage = QImage("Slide03.png")
		palette = QPalette()
		palette.setBrush(10, QBrush(oImage))
		self.setPalette(palette)
		self.show()
		timer = QTimer(self)
		timer.timeout.connect(self.thirdImage)
		timer.setSingleShot(True)
		timer.start(3000)

	def thirdImage(self):
		oImage = QImage("Slide04.png")
		palette = QPalette()
		palette.setBrush(10, QBrush(oImage))
		self.setPalette(palette)
		self.show()
		timer = QTimer(self)
		timer.timeout.connect(self.fourthImage)
		timer.setSingleShot(True)
		timer.start(3000)

	def fourthImage(self):
		oImage = QImage("Slide05.png")
		palette = QPalette()
		palette.setBrush(10, QBrush(oImage))
		self.setPalette(palette)
		self.show()
		timer = QTimer(self)
		timer.timeout.connect(self.fifthImage)
		timer.setSingleShot(True)
		timer.start(3000)

	def fifthImage(self):
		oImage = QImage("Slide06.png")
		palette = QPalette()
		palette.setBrush(10, QBrush(oImage))
		self.setPalette(palette)
		self.show()
		timer = QTimer(self)
		timer.timeout.connect(self.gameSlide)
		timer.setSingleShot(True)
		timer.start(3000)

	def gameSlide(self):
		palette = QPalette()
		palette.setBrush(10, QBrush(Qt.black))
		self.setPalette(palette)

		self.timerDisplay = QLabel("Time remaining: 60 seconds")
		self.timerDisplay.setStyleSheet("background-color: black; color: white")
		self.questionText = QLabel()
		self.questionText.setStyleSheet("background-color: black; color: white")
		self.answer = QLabel()
		self.answer.setStyleSheet("background-color: black; color: white")
		self.answer.setWordWrap(True)
		self.leftDoor = QPushButton(self)
		self.leftDoor.clicked.connect(self.choseLeft)
		self.leftDoor.setIcon(QIcon("Door.png"))
		self.leftDoor.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
		self.leftDoor.setIconSize(QSize(300, 250))
		self.leftDoor.setStyleSheet("background-color: black")
		self.rightDoor = QPushButton(self)
		self.rightDoor.clicked.connect(self.choseRight)
		self.rightDoor.setIcon(QIcon("Door.png"))
		self.rightDoor.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
		self.rightDoor.setIconSize(QSize(300, 250))
		self.rightDoor.setStyleSheet("background-color: black")

		self.level = 0
		self.difficulty = 1
		self.gameOver = False
		self.startGame()

		self.vbox = QVBoxLayout()
		self.vbox.addWidget(self.timerDisplay)
		self.vbox.addWidget(self.questionText)
		self.vbox.addWidget(self.answer)

		self.hbox = QHBoxLayout()
		self.hbox.addWidget(self.leftDoor)
		self.hbox.addWidget(self.rightDoor)

		self.vbox.addLayout(self.hbox)

		self.setLayout(self.vbox)

		self.show()

	def choseLeft(self):
		self.gameTimer.stop()
		self.displayUpdate.stop()
		self.timerDisplay.hide()
		self.questionText.hide()
		self.answer.hide()
		self.leftDoor.hide()
		self.rightDoor.hide()
		if self.safe == 0:
			if self.level == 19:
				self.penultimateProblem()
			elif self.level == 20:
				self.startGame()
			else:
				oImage = QImage("Slide06.png")
				palette = QPalette()
				palette.setBrush(10, QBrush(oImage))
				self.setPalette(palette)
				self.show()
				timer = QTimer(self)
				timer.timeout.connect(self.startGame)
				timer.setSingleShot(True)
				timer.start(3000)
		else:
			self.gameOver = True
			self.startGame()

	def choseRight(self):
		self.gameTimer.stop()
		self.displayUpdate.stop()
		self.timerDisplay.hide()
		self.questionText.hide()
		self.answer.hide()
		self.leftDoor.hide()
		self.rightDoor.hide()
		if self.safe == 1:
			if self.level == 19:
				self.penultimateProblem()
			elif self.level == 20:
				self.startGame()
			else:
				oImage = QImage("Slide06.png")
				palette = QPalette()
				palette.setBrush(10, QBrush(oImage))
				self.setPalette(palette)
				self.show()
				timer = QTimer(self)
				timer.timeout.connect(self.startGame)
				timer.setSingleShot(True)
				timer.start(3000)
		else:
			self.gameOver = True
			self.startGame()

	def penultimateProblem(self):
		self.timerDisplay.hide()
		self.questionText.hide()
		self.answer.hide()
		self.leftDoor.hide()
		self.rightDoor.hide()
		oImage = QImage("Slide09.png")
		palette = QPalette()
		palette.setBrush(10, QBrush(oImage))
		self.setPalette(palette)
		self.show()
		timer = QTimer(self)
		timer.timeout.connect(self.showDoors)
		timer.setSingleShot(True)
		timer.start(3000)

	def showDoors(self):
		oImage = QImage("Slide06.png")
		palette = QPalette()
		palette.setBrush(10, QBrush(oImage))
		self.setPalette(palette)
		self.show()
		timer = QTimer(self)
		timer.timeout.connect(self.startGame)
		timer.setSingleShot(True)
		timer.start(3000)

	def buildExpression(self, depth):

		operatorChoice = random.choice(self.operators)

		if depth > 1:
			return "(" + self.buildExpression(depth - 1) + " " + operatorChoice + " " + self.buildExpression(depth - 1) + ")"
		else :
			return "(" + random.choice(self.values) + " " + operatorChoice + " " + random.choice(self.values) + ")"

	def expressionSolver(self, exp):
		parens = 0
		for character in exp:
			if character == "(" or character == ")":
				parens += 1

		if parens <= 2:
			leftVar = exp[1:2]
			rightVar = exp[-2:-1]
			fn = exp[3:-3]
			solver = self.operatorValues.get(fn)
			return solver(self.booleanValues.get(leftVar),self.booleanValues.get(rightVar))
		else:
			i = (parens / 2) - 1
			leftString = ""
			counter = 1
			while i > 0:
				if exp[counter] == "(" or exp[counter] == ")":
					i -= 1
				leftString += exp[counter]
				counter += 1
			operatorStart = counter
			i = (parens / 2) - 1
			rightString = ""
			counter = len(exp) - 2
			while i > 0:
				if exp[counter] == "(" or exp[counter] == ")":
					i -= 1
				rightString += exp[counter]
				counter -= 1
			rightString = rightString[::-1]
			operatorEnd = counter
			fn = exp[operatorStart:operatorEnd].strip()
			solver = self.operatorValues.get(fn)
			return solver(self.expressionSolver(leftString), self.expressionSolver(rightString))

	# MARK: --GAME LEVEL CODE--
	def startGame(self):
		if not(self.gameOver) and self.difficulty < 5:
			palette = QPalette()
			palette.setBrush(10, QBrush(Qt.black))
			self.setPalette(palette)
			self.timerDisplay.show()
			self.questionText.show()
			self.answer.show()
			self.leftDoor.show()
			self.rightDoor.show()
			self.gameSeconds = 60
			self.timerDisplay.setText("Time remaining: 60 seconds")
			self.level += 1
			if self.level % 5 == 0:
				self.difficulty += 1
			questionChoice = random.choice(self.questions)
			expression = self.buildExpression(self.difficulty)
			result = self.expressionSolver(expression)
			self.safe = 0 # 0 means left door, 1 means right door
			if questionChoice == self.questions[0]:
				if result:
					self.safe = 0
				else:
					self.safe = 1
			elif questionChoice == self.questions[1]:
				if result:
					self.safe = 1
				else:
					self.safe = 0
			elif questionChoice == self.questions[2]:
				if result:
					self.safe = 1
				else:
					self.safe = 0
			else:
				if result:
					self.safe = 0
				else:
					self.safe = 1

			self.displayUpdate = QTimer(self)
			self.displayUpdate.timeout.connect(self.updateWindow)
			self.displayUpdate.setSingleShot(False)
			self.displayUpdate.start(1000)

			self.gameTimer = QTimer(self)
			self.gameTimer.timeout.connect(self.endGame)
			self.gameTimer.setSingleShot(True)
			self.gameTimer.start(60000)
			self.questionText.setText(questionChoice)
			self.answer.setText(expression)
		elif self.difficulty == 5:
			self.questionText.hide()
			self.timerDisplay.hide()
			self.answer.hide()
			self.leftDoor.hide()
			self.rightDoor.hide()
			oImage = QImage("Slide10.png")
			palette = QPalette()
			palette.setBrush(10, QBrush(oImage))
			self.setPalette(palette)
			self.show()
		else:
			self.questionText.hide()
			self.timerDisplay.hide()
			self.answer.hide()
			self.leftDoor.hide()
			self.rightDoor.hide()
			oImage = QImage("Slide08.png")
			palette = QPalette()
			palette.setBrush(10, QBrush(oImage))
			self.setPalette(palette)
			self.show()

	def updateWindow(self):
		self.gameSeconds -= 1
		timerDisplayText = "Time remaining: " + str(self.gameSeconds) + " seconds"
		self.timerDisplay.setText(timerDisplayText)

	def endGame(self):
		self.timerDisplay.hide()
		self.questionText.hide()
		self.answer.hide()
		self.leftDoor.hide()
		self.rightDoor.hide()
		oImage = QImage("Slide07.png")
		palette = QPalette()
		palette.setBrush(10, QBrush(oImage))
		self.setPalette(palette)
		self.show()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    window = GameWindow()
    sys.exit(app.exec_())



