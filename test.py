import unittest2
import ScheduleAlert

class ScheduleAlertTestCase(unittest2.TestCase):
    def setUp(self):
        self.sa = ScheduleAlert
    def tearDown(self):
        self.sa = None

    def test_diffTime(self):
        self.assertEqual(5, self.sa.diffTime('17:00:05', '17:00:10'))

    def test_timeinseconds(self):
        self.assertEqual(3661, self.sa.timeinseconds('1:1:1'))

    def test_checkFaile(self):
        self.assertFalse(self.sa.checkFaile("17:00:00"))
        self.assertTrue(self.sa.checkFaile("25:60:60"))
        self.assertTrue(self.sa.checkFaile("17:00"), "")

    def test_validTime(self):
        self.assertFalse(self.sa.validTime(25,60,60))
        self.assertTrue(ScheduleAlert.validTime(23, 59, 59))


    # def test_httpGet(self):
    #     result = app.httpGet('http://freegeoip.net/json')
    #     self.assertRaises(ValueError, result):
    #
    # def test_httpResponse(self):
    #     res.txt =  {'latitude': j['latitude'], 'longitude': j['longitude']}
    #     result = app.httpResponse(res)
    #     expected =  "No data response"
    #     self.assertEqual(result, expected)
    #
    # def test_getCoordinate(self):
    #     c = app.getCoordinate()
    #     result = {'latitude': c['latitude'], 'longitude': c['longitude']}
    #     expected = self.assertEqual(c['latitude'], expected, "latitude is Null")

if __name__ == '__main__':
    unittest2.main()