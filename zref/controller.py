import sys
from functools import partial
from PyQt5.QtWidgets import *

from model import evaluateExpression
from view import PyCalcUi


class PyCalcCtrl:
    def __init__(self, view, model):
        self._evalute = model
        self._view = view
        self._connectSignals()

    def _calculateResult(self):
        res = self._evalute(expression=self._view.displayText())
        self._view.setDisplayText(res)

    def _buildExpression(self, sub_exp):
        if self._view.displayText() == "Error":
            self._view.clearDisplay()

        expression = self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)

    def _connectSignals(self):
        for btnText, btn in self._view.buttons.items():
            if btnText not in {'=', 'C'}:
                btn.clicked.connect(partial(self._buildExpression, btnText))

        self._view.buttons['C'].clicked.connect(self._view.clearDisplay)
        self._view.buttons['='].clicked.connect(self._calculateResult)
        # self._view.display.returnPressed.connect(self._calculateResult)

def main():
    pycalc = QApplication([])
    view = PyCalcUi()
    view.show()

    model = evaluateExpression

    PyCalcCtrl(view=view, model=model)
    sys.exit(pycalc.exec_())

if __name__ == '__main__':
    main()