from django.test import SimpleTestCase

# Create your tests here.


class TestNearHundred(SimpleTestCase):
    def test_near_hundred_93(self):
        response = self.client.get("/warmup1/near-hundred/190/")
        self.assertContains(response, "True")

    def test_near_hundred_90(self):
        response = self.client.get("/warmup1/near-hundred/90/")
        self.assertContains(response, "True")

    def test_near_hundred_89(self):
        response = self.client.get("/warmup1/near-hundred/189/")
        self.assertContains(response, "False")


class TestStringSplosion(SimpleTestCase):
    def test_string_splosion_CCoCodCode(self):
        response = self.client.get("/warmup2/string-splosion/Code/")
        self.assertContains(response, "CCoCodCode")

    def test_string_splosion_abc(self):
        response = self.client.get("/warmup2/string-splosion/abc/")
        self.assertContains(response, "aababc")

    def test_string_splosion_ab(self):
        response = self.client.get("/warmup2/string-splosion/ab/")
        self.assertContains(response, "aab")


class TestCatDog(SimpleTestCase):
    def test_cat_dog_catdog(self):
        response = self.client.get("/string2/cat-dog/catdog/")
        self.assertContains(response, "True")

    def test_cat_dog_catcat(self):
        response = self.client.get("/string2/cat-dog/catcat/")
        self.assertContains(response, "False")

    def test_cat_dog_1cat1cadodog(self):
        response = self.client.get("/string2/cat-dog/1cat1cadodog/")
        self.assertContains(response, "True")


class TestLoneSum(SimpleTestCase):
    def test_lone_sum_123(self):
        response = self.client.get("/logic2/lone-sum/1/2/3/")
        self.assertContains(response, "6")

    def test_lone_sum_323(self):
        response = self.client.get("/logic2/lone-sum/3/2/3/")
        self.assertContains(response, "2")

    def test_lone_sum_333(self):
        response = self.client.get("/logic2/lone-sum/3/3/3/")
        self.assertContains(response, "0")
