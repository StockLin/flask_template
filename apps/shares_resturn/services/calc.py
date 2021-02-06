class Calculator:
    def __init__(self):
        pass

    def add(self, x=0, y=0):
        try:
            if x and y:
                return x + y

            return 0

        except Exception as e:
            raise e

    def substract(self, x=0, y=0):
        try:
            if x and y:
                return x - y

            return 0

        except Exception as e:
            raise e