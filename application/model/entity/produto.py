class Produto:
    def __init__(self, id, name, image, oldPrice, price, description, installments, installments_value):
        self._id = id
        self._name = name
        self._image = image
        self._oldPrice = oldPrice
        self._price = price
        self._description = description
        self._installments = installments
        self._installments_value = installments_value


    def getName(self):
        return self._name

    def getId(self):
        return self._id

    def getImage(self):
        return self._image

    def getOldPrice(self):
        return self._oldPrice

    def getPrice(self):
        return self._price

    def getDescription(self):
        return self._description

    def getInstallments(self):
        return self._installments

    def get_installments_value(self):
        return self._installments_value