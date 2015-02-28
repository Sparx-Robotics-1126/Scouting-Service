from google.appengine.ext import ndb

class ScoutingAuto(ndb.Model):
    startingLocationX = ndb.FloatProperty()
    startingLocationY = ndb.FloatProperty()
    isRobotInAutoZone = ndb.BooleanProperty()
    isRobotCreateStack = ndb.BooleanProperty()
    totesMovedToAutoZone = ndb.IntegerProperty()
    rcMovedToAutoZone = ndb.IntegerProperty()
    rcTakenFromStep = ndb.IntegerProperty()
    endingLocationX = ndb.FloatProperty()
    endingLocationY = ndb.FloatProperty()
	
class ScoutingTele(ndb.Model):
    totesStacked1 = ndb.IntegerProperty()
    totesStacked2 = ndb.IntegerProperty()
    totesStacked3 = ndb.IntegerProperty()
    totesStacked4 = ndb.IntegerProperty()
    rcStacked1 = ndb.BooleanProperty()
    rcStacked2 = ndb.BooleanProperty()
    rcStacked3 = ndb.BooleanProperty()
    rcStacked4 = ndb.BooleanProperty()
    litter1 = ndb.BooleanProperty()
    litter2 = ndb.BooleanProperty()
    litter3 = ndb.BooleanProperty()
    litter4 = ndb.BooleanProperty()

class ScoutingGeneral(ndb.Model):
    numberOfPenalties = ndb.IntegerProperty()
    numberOfStacksTipped = ndb.IntegerProperty()
    numberOfFailedAttemptsOfRC = ndb.IntegerProperty()
    numberOfRCTakenFromStep = ndb.IntegerProperty()
    isDead = ndb.BooleanProperty()
    isTipped = ndb.BooleanProperty()
    numberOfTotesAcquiredFromHP = ndb.IntegerProperty()
    numberOfTotesAttemptedFromHP = ndb.IntegerProperty()
    numberOfTotesFromLandfill = ndb.IntegerProperty()
    generalComments = ndb.StringProperty()
    commentsOnPenalties = ndb.StringProperty()

class Scouting(ndb.Model):
    nameOfScouter = ndb.StringProperty()
    teamKey = ndb.StringProperty()
    eventKey = ndb.StringProperty()
    matchKey = ndb.StringProperty()

    auto = ndb.StructuredProperty(ScoutingAuto, repeated=False)
    tele = ndb.StructuredProperty(ScoutingTele, repeated=False)
    general = ndb.StructuredProperty(ScoutingGeneral, repeated=False)
