from app.Building import Building
from app.Zone import Zone

class Map(object):
	def __init__(self):
		self.Zones = []
		self.BuildingModels = {}

	def canBuildOnZone(self, Zone):
		return Zone.collidelist(self.Zones) == False

	def createBuilding(self, modelName, position):
		Model = self.BuildingModels[modelName]

		BuildingZone = Zone(position, (Model.Zone.w, Model.Zone.h))
		if not self.canBuildOnZone(BuildingZone): raise ValueError("Trying to build on occupied zone.") 
		
		B = Building(Model.life, Model.affiliation, BuildingZone)
		return B
