import unittest

class MapTestCase(unittest.TestCase):

    def test_map_create_building_success(self):
        M = Map()

        Zone1 = Zone((0, 0), (10, 4))
        Zone2 = Zone((0, 0), (3, 10))
        Zone3 = Zone((0, 6), (10, 4))
        Zone4 = Zone((4, 0), (6, 10))
        M.Zones = [Zone1, Zone2, Zone3, Zone4]

        Model = Building(life = 10, affiliation = 0, Zone = Zone((0, 0), (1, 2)))
        M.BuildingModels["Test Model"] = Model

        x, y = 3, 4

        B = Map.createBuilding(name = "Test Model", position = (x, y))
        assert B.life == Model.life
        assert B.Zone.x == x
        assert B.Zone.y == y
        assert B.Zone.width == Model.Zone.width
        assert B.Zone.height == Model.Zone.height
        assert B.affiliation == Model.affiliation

    def test_map_create_building_failure_collision(self):
        M = Map()

        Zone1 = Zone((0, 0), (10, 10))
        M.Zones = [Zone1]

        Model = Building(life = 10, affiliation = 0, Zone = Zone((0, 0), (1, 2)))
        M.BuildingModels["Test Model"] = Model

        x, y = 3, 4
        self.assertRaises(ValueError, M.createBuilding, ["Test Model", (x, y)])

    def test_map_create_building_failure_wrong_model_name(self):
        M = Map()

        Zone1 = Zone((0, 0), (10, 10))
        M.Zones = [Zone1]

        Model = Building(life = 10, affiliation = 0, Zone = Zone((0, 0), (1, 2)))
        M.BuildingModels["Test Model"] = Model

        x, y = 3, 4
        self.assertRaises(KeyError, M.createBuilding, ["Invalid Test Model", (x, y)])
