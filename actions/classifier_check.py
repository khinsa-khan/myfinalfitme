class Classifier_check(object):
    def recommend_size(self, chest1):
        if chest1 < 32:
            return (str("XS"))
        if chest1 >= 32 and chest1 < 37:
            return (str("S"))
        if chest1 >= 37 and chest1 < 40:
            return (str("M"))
        if chest1 >= 40 and chest1 < 44:
            return (str("L"))
        if chest1 >= 44 and chest1 < 48:
            return (str("XL"))
        if chest1 >= 48 and chest1 < 52:
            return (str("2XL"))
        if chest1 >= 52 and chest1 < 56:
            return (str("3XL"))
        if chest1 >= 56 and chest1 < 60:
            return (str("4XL"))
        if chest1 > 60:
            return (str("5XL"))
