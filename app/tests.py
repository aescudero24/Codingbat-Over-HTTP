from django.test import SimpleTestCase

# Create your tests here.


class TestNearHundred(SimpleTestCase):
    def test_near_hundred_99(self):
        response = self.client.get("/warmup1/near-hundred/190/")
        self.assertContains(response, "True")

    def test_near_hundred_90(self):
        response = self.client.get("/warmup1/near-hundred/90/")
        self.assertContains(response, "True")

    def test_near_hundred_89(self):
        response = self.client.get("/warmup1/near-hundred/189/")
        self.assertContains(response, "False")


class TestStringSplosion(SimpleTestCase):
    def test_string_splosion_apple(self):
        response = self.client.get("/warmup2/string-splosion/apple/")
        self.assertContains(response, "aapappapplapple")

    def test_string_splosion_adrian(self):
        response = self.client.get("/warmup2/string-splosion/adrian/")
        self.assertContains(response, "aadadradriadriaadrian")

    def test_string_splosion_BCCA(self):
        response = self.client.get("/warmup2/string-splosion/BCCA/")
        self.assertContains(response, "BBCBCCBCCA")


class TestCatDog(SimpleTestCase):
    def test_cat_dog_catdog(self):
        response = self.client.get("/string2/cat-dog/catdog/")
        self.assertContains(response, "True")

    def test_cat_dog_applecat(self):
        response = self.client.get("/string2/cat-dog/applecat/")
        self.assertContains(response, "False")

    def test_cat_dog_appledogorangecat(self):
        response = self.client.get("/string2/cat-dog/appledogorangecat/")
        self.assertContains(response, "True")


class TestLoneSum(SimpleTestCase):
    def test_lone_sum_321(self):
        response = self.client.get("/logic2/lone-sum/3/2/1/")
        self.assertContains(response, "6")

    def test_lone_sum_122(self):
        response = self.client.get("/logic2/lone-sum/1/2/2/")
        self.assertContains(response, "3")

    def test_lone_sum_369(self):
        response = self.client.get("/logic2/lone-sum/3/6/9/")
        self.assertContains(response, "18")
