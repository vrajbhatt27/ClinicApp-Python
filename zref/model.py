
def evaluateExpression(expression):
    try:
        res = str(eval(expression, {}, {}))
    except Exception as e:
        res = "Error"

    return res