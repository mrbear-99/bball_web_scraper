from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

def get_game_info():
    PATH = '/Users/isaacmeltsner/Desktop/Bball_twitter_bot/chromedriver'
    driver = webdriver.Chrome(PATH)
    driver.get('https://www.basketball-reference.com/')
    try:
        scores = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Scores')))
        scores.click()
        box_score = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Box Score')))
        box_score = driver.find_elements(By.LINK_TEXT, 'Box Score')
        all_games = []
        for game in range(len(box_score)):
            box_score[game].click()
            score_info = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'scorebox')))
            score_info = score_info.text.split('\n')
            team1_name, team1_score = score_info[0], score_info[1]
            team2_name, team2_score = score_info[4], score_info[5]
            game_info = (f'Game at {score_info[8]}\n{team1_name}: {team1_score}\n{team2_name}: {team2_score}')
            all_games.append(game_info)
            driver.back()
            box_score = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Box Score')))
            box_score = driver.find_elements(By.LINK_TEXT, 'Box Score')
    except NoSuchElementException:
        print('Not Found')
    driver.quit()
    return all_games

if __name__ == '__main__':
    todays_games = get_game_info()
    for i in todays_games:
        print(i)
