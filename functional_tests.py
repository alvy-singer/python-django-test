from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 伊迪斯听说有一个很酷的在线待办事项应用
        # 她去看了这个应用的首页
        self.browser.get('http://localhost:8000')

        # 她注意到网页的标题和头部都包含'To-Do'这个词
        self.assertIn('To-Do', self.browser.title)
        header_test = self.browser.find_element_by_tag_name('h1').test
        self.assertIn('To-Do', header_test)

        # 应用邀请她输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # 她在文本框里输入'buy peacock feathers'
        # 伊迪斯的爱好是使用苍蝇做鱼饵钓鱼
        inputbox.send_keys('buy peacock feathers')
        # 她按回车键后, 页面更新了
        # 代办事项表格中显示了'1: buy peacock feather'
        inputbox.send_key(Keys.Enter)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_id('tr')
        self.assertTrue(any(row.text == '1: buy peacock feather' for row in rows))

        self.fail('Finish the test')


if __name__ == '__main__':
    unittest.main()
