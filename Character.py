class Character():
    
    def __init__(self, name, isWoman, haveLongHair, haveCurlyHair, haveGreyHair, useGlasses, isNigga, isTall, isDoctor, haveFacialHair, haveBeard, haveMoustache):
        self.name = str(name)
        self.isWoman = bool(isWoman)
        self.haveLongHair = bool(haveLongHair)
        self.haveCurlyHair = bool(haveCurlyHair)
        self.haveGreyHair = bool(haveGreyHair)
        self.useGlasses = bool(useGlasses)
        self.isNigga = bool(isNigga)
        self.isTall = bool(isTall)
        self.isDoctor = bool(isDoctor)
        self.haveFacialHair = bool(haveFacialHair)
        self.haveBeard = bool(haveBeard)
        self.haveMoustache = bool(haveMoustache)

    def getQualities(self):
        characterDict = {
            'name': self.name,
            'isWoman': self.isWoman,
            'haveLongHair': self.haveLongHair,
            'haveCurlyHair': self.haveCurlyHair,
            'haveGreyHair': self.haveGreyHair,
            'useGlasses': self.useGlasses,
            'isNigga': self.isNigga,
            'isTall': self.isTall,
            'isDoctor': self.isDoctor,
            'haveFacialHair': self.haveFacialHair,
            'haveBeard': self.haveBeard,
            'haveMoustache': self.haveMoustache
        }
        return characterDict
