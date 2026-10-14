class Event:
    def __init__(self, IDnum, Name, Message, Sector, Effect):
        self.IDnum = IDnum
        self.name = Name
        self.msg = Message
        self.sector = Sector
        self.effect = Effect # + or - in percentage