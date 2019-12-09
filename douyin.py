import json,os,time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class douyin:
    
    def __init__(self,wait_time = 20,cookies = None):
        self.cookies = None
        if cookies is None:
            try:
                with open('cookies.dat','r+') as f:
                    cookie = f.read()
                if cookie is not None:
                    self.cookies = json.loads(cookie)
            except:
                pass
        else:
            self.cookies = cookies
        o = webdriver.ChromeOptions()
        o.add_argument('--log-level=3')
        o.add_experimental_option('excludeSwitches',['enable-automation'])
        self.web = webdriver.Chrome(options=o)
        self.web.set_page_load_timeout(wait_time)
        self.web.set_script_timeout(wait_time)
        self.web_wait = WebDriverWait(self.web, wait_time)

    def run(self,video_path,title,i_look = 2,i_save = 1):
        """
        :param video_path: 视频路径地址
        :param title: 视频描述标题
        :param i_look: 0表示公开 1表示好友可见 2表示自己可见
        :param i_save: 0表示允许别人保存 1表示不允许别人保存
        """
        while not dy.login():
            time.sleep(1)
        dy.getinfo()
        try:
            dy.upload(video_path,title,i_look,i_save)
        except:
            print('上传抖音视频失败')
        finally:
            time.sleep(10)
            self.webquit()
    
    def login(self):
        print('开始登录......')
        try:
            self.web.get('https://sso.douyin.com/?service=https://www.douyin.com/login/type/media#/')
            if self.cookies is not None:
                for i in self.cookies:
                    if 'expiry' in i:
                        #删除指定键值
                        i.pop('expiry')
                    self.web.add_cookie(i)
                self.web.refresh()
            num = 0
            while True:
                print('获取登录状态中......')
                if self.web.current_url == 'https://media.douyin.com/#/upload':
                    print('账号登录成功')
                    cookies = json.dumps(self.web.get_cookies())
                    with open('cookies.dat','w+') as f:
                        f.write(cookies)
                    return True
                elif num > 30:
                    num = 0
                    print('仍然未登录到抖音 刷新网页！')
                    self.web.refresh()
                else:
                    time.sleep(3)
                    num += 1
        except :
            self.web.execute_script('window.stop ? window.stop() : document.execCommand("Stop");')
        return False

    def getinfo(self):
        locate = (By.XPATH,'//*[@id="root"]/div/div[1]/div/div[1]/div[1]/div')
        user_name = self.web_wait.until(EC.presence_of_element_located(locate)).get_attribute('innerHTML')
        locate = (By.XPATH,'//*[@id="root"]/div/div[1]/div/div[1]/div[2]/div[1]/div[1]')
        likes = self.web_wait.until(EC.presence_of_element_located(locate)).get_attribute('innerHTML')
        locate = (By.XPATH,'//*[@id="root"]/div/div[1]/div/div[1]/div[2]/div[3]/div[1]')
        fans = self.web_wait.until(EC.presence_of_element_located(locate)).get_attribute('innerHTML')
        tmp = '用户名：%s 获赞数：%s 粉丝数：%s' % (user_name,likes,fans)        
        print(tmp)
    
    def upload(self,video_path,title,i_look = 2,i_save = 1):
        print('上传视频文件中....')
        locator = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[4]/div[1]/label/input')
        self.web_wait.until(EC.presence_of_element_located(locator)).send_keys(video_path)

        locate = (By.XPATH,'//*[@id="root"]/div/div[2]/div/div[5]/div[1]/div[2]/div[1]/div[1]/div[2]/div/div/div/div')
        self.web_wait.until(EC.presence_of_element_located(locate)).click()
        print('完善视频详情.....')
        self.web_wait.until(EC.presence_of_element_located(locate)).send_keys(title)
        time.sleep(1)
        if i_look > 0 :
            locate = (By.XPATH,'//*[@id="root"]/div/div[2]/div/div[5]/div[1]/div[4]/label[%s]' % str(i_look + 1))
            self.web_wait.until(EC.presence_of_element_located(locate)).click()
        if i_save == 0 :
            locate = (By.XPATH,'//*[@id="root"]/div/div[2]/div/div[5]/div[1]/div[6]/div/label[1]/svg')
            self.web_wait.until(EC.presence_of_element_located(locate)).click()
        locate = (By.XPATH,'//*[@id="root"]/div/div[2]/div/div[5]/div[1]/div[8]/button[1]')
        self.web_wait.until(EC.presence_of_element_located(locate)).click()
        print('发布视频中...')
        num = 0
        while True:
            time.sleep(3)
            if self.web.current_url == 'https://media.douyin.com/#/manage':
                print('视频发布成功')
                break
            else:
                num += 1
                if num > 10:
                    print('视频发布超时')
                    break

    def webquit(self):
        print('退出脚本，关闭浏览器...')
        if self.web is not None:
            self.web.close()
            
if __name__ == "__main__":
    dy = douyin()
    dy.run('/Users/mysite/Downloads/薏米茶.mp4','这里是视频标题')