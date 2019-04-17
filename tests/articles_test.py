import unittest
from app.models import Articles

class ArticlesTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the class
    '''
    
    def setUp(self):
        '''
        setUp method that will run before every test
        '''
        self.new_article = Articles("abc-news","Abc","associated","a 5o year old","https:\/\/abcnews.go.com\/US\/wireStory\/louisiana-man-charged-100-counts-degree-rape-62425650","https:\/\/s.abcnews.com\/images\/US\/mississippi-storm-damage-ap-mo-20190414_hpMain_16x9_992.jpg","2019-04-16T09:36:47Z","The number of tornadoes confirmed over the weekend ha")
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))
        
if __name__ == '__main__':