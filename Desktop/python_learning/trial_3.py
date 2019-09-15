
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# 各種設定
# twitterアカウント
account = 'FishLot'
password = 'Hrkmrk455'
# 返答したい投稿のURL
tweet_url = "https://twitter.com/FishLot/status/1171785444788297730?s=20"
# 返答したいテキスト
reply_text = '''test from selenium'''

# Twitterログイン実行する処理
def twitterlogin():
    # ログインページを開く
    driver.get('https://twitter.com/login/')
    time.sleep(3)  # 動作止める
    # accountを入力する
    element_account = driver.find_element_by_class_name("js-username-field")
    element_account.send_keys(account)
    time.sleep(3)  # 動作止める
    # パスワードを入力する
    element_pass = driver.find_element_by_class_name("js-password-field")
    element_pass.send_keys(password)
    time.sleep(3)  # 動作止める
    # ログインボタンをクリックする
    element_login = driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    element_login.click()
    time.sleep(3)  # 動作止める

# Tweetリプライ実行する処理
def tweetreply(tweet_url):
    # ツイートIDを取得する
    tweetID = tweet_url[-19:]
    driver.get(tweet_url)
    try:
        # 投稿文を挿入
        driver.find_element_by_id("tweet-box-reply-to-" + tweetID).click()
        time.sleep(3)  # 動作止める
        driver.find_element_by_id("tweet-box-reply-to-" + tweetID).click()
        time.sleep(3)  # 動作止める
        driver.find_element_by_id("tweet-box-reply-to-" + tweetID).send_keys(reply_text)
        time.sleep(3)  # 動作止める
        driver.find_element_by_id("tweet-box-reply-to-" + tweetID).send_keys(Keys.CONTROL + "\n")
    except:
        print("Error")


# selenium起動
options=Options()
driver=webdriver.Chrome()

# Twitterログイン処理
twitterlogin()
# Tweetリプライ処理
tweetreply(tweet_url)

# seleniumを終了
driver.close()
driver.quit()
