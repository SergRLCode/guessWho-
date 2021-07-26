class Character():
    
    def __init__(self, name, isWoman, looksYoung, haveLongHair, haveCurlyHair, haveFlamboyantColorHair, haveGreyHair, haveBlackHair, haveBrownHair, isBlonde, isRedhead, useGlasses, isNigga, isTall, isThin, haveFacialHair, haveBeard, haveMoustache, useMakeup):
            self.name = str(name)
            self.isWoman = bool(isWoman)
            self.looksYoung = bool(looksYoung)
            self.haveLongHair = bool(haveLongHair)
            self.haveCurlyHair = bool(haveCurlyHair)
            self.haveFlamboyantColorHair = bool(haveFlamboyantColorHair)
            self.haveGreyHair = bool(haveGreyHair)
            self.haveBlackHair = bool(haveBlackHair)
            self.haveBrownHair = bool(haveBrownHair)
            self.isBlonde = bool(isBlonde)
            self.isRedhead = bool(isRedhead)
            self.useGlasses = bool(useGlasses)
            self.isNigga = bool(isNigga)
            self.isTall = bool(isTall)
            self.isThin = bool(isThin)
            self.haveFacialHair = bool(haveFacialHair)
            self.haveBeard = bool(haveBeard)
            self.haveMoustache = bool(haveMoustache)
            self.useMakeup = bool(useMakeup)

    def getQualities(self):
        return {
            'name': self.name,
            'isWoman': self.isWoman,
            'looksYoung': self.looksYoung,
            'haveLongHair': self.haveLongHair,
            'haveCurlyHair': self.haveCurlyHair,
            'haveFlamboyantColorHair': self.haveFlamboyantColorHair,
            'haveGreyHair': self.haveGreyHair,
            'haveBlackHair': self.haveBlackHair,
            'haveBrownHair': self.haveBrownHair,
            'isBlonde': self.isBlonde,
            'isRedhead': self.isRedhead,
            'useGlasses': self.useGlasses,
            'isNigga': self.isNigga,
            'isTall': self.isTall,
            'isThin': self.isThin,
            'haveFacialHair': self.haveFacialHair,
            'haveBeard': self.haveBeard,
            'haveMoustache': self.haveMoustache,
            'useMakeup': self.useMakeup
        }
