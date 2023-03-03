import pygame
import sys
import random
from tkinter import messagebox

screen = pygame.display.set_mode((1280,960)) # スクリーン初期化 解像度設定

img_bg = pygame.image.load("img\\bg_space.png") # 背景画像
img_chara = [pygame.image.load("img\ch_bird_1.png"), # 主人公の画像
             pygame.image.load("img\ch_bird_2.png"),
             pygame.image.load("img\ch_bird_died.png")
             ]
img_tama = pygame.image.load("img\\tama.png") # 弾の画像
img_tama_2 = pygame.image.load("img\\tama_2.png") # 弾の画像

tmr = 0 # 時間管理変数
idx = 0
ch_x = 565 # 主人公のX座標 初期化
ch_y = 810 # 同じくY座標
CH_SPD = 10 # 主人公の速さ
TA_MAX = 100 # 弾の量
ta_x = [-100]*TA_MAX # 弾のX座標 初期化
ta_y = [-100]*TA_MAX # 同じくY座標
ta_kazu = TA_MAX # 弾の数
TA_SPD = 10 # 弾の速さ
ta_kakuritsu = 1
TA_2_KAZU = 200 # 一度に画面に描画される最大量
ta_2_x = [-100]*TA_2_KAZU # 弾のX座標 初期化 #弾2は主人公が出す弾
ta_2_y = [-100]*TA_2_KAZU # 同じくY座標
ta_utsu = 0
gmov = 0 # ゲームオーバーの原因の玉
msbx = 0 # メッセージボックス
ATARIHANTEI_X = 35 # 35
ATARIHANTEI_Y = 40 # 40


def control(): # 主人公の操作
    global ch_x, ch_y, ta_utsu
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]: 
        ch_y = ch_y - CH_SPD
        if ch_y < 0:
            while ch_y < 0:
                ch_y = ch_y + 1
    if key[pygame.K_DOWN]:
        ch_y = ch_y + CH_SPD
        if ch_y > 810:
             while ch_y > 810:
                ch_y = ch_y - 1
    if key[pygame.K_RIGHT]:
        ch_x = ch_x + CH_SPD
        if ch_x > 1130:
            while ch_x > 1130:
                ch_x = ch_x - 1
    if key[pygame.K_LEFT]:
        ch_x = ch_x - CH_SPD
        if ch_x < 0:
            while ch_x < 0:
                ch_x = ch_x + 1
    ta_utsu = (ta_utsu+1)*key[pygame.K_z] # 弾を打つ
    if ta_utsu%5 == 1:
        ta_utsu = 1

def event():
    global idx, ta_utsu
    pygame.event.pump() # よくわからん。おまじないらしい。
    key = pygame.key.get_pressed() # キーが押されているかを取得
    for event in pygame.event.get(): # WIndowのバツボタンが押されたとき
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                idx = 0

def tama():
    global ta_kakuritsu, gmov, idx, screen
    t = 0
    ta_kakuritsu = 1
    for i in range(ta_kazu):
        if ta_y[i] != -100: # 有効なら
            ta_y[i] = ta_y[i] + TA_SPD # 弾を動かす
            if ta_y[i] > 960: # 画面外なら
                ta_y[i] = -100 # 無効化
            else:
                dx = abs((ch_x+75) - (ta_x[i]+15))
                dy = abs((ch_y+75) - (ta_y[i]+60))
                if dx <= ATARIHANTEI_X and dy <= ATARIHANTEI_Y:
                    gmov = i
                    idx = 2
                screen.blit(img_tama, [ta_x[i], ta_y[i]]) # 描画
        else:   
            if t == 0:
                r = random.randint(1,100)
                if r <= ta_kakuritsu: # 確率で弾が出現
                    t = 1
                    ta_y[i] = -90
                    r = random.randint(0,1250) # 弾のX座標
                    ta_x[i] = r
                    screen.blit(img_tama, [ta_x[i], ta_y[i]]) # 描画
            elif t == 1:
                r = random.randint(1,500)
                if r <= ta_kakuritsu: # 確率で弾が出現
                    t = 2
                    ta_y[i] = -90
                    r = random.randint(0,1250) # 弾のX座標
                    ta_x[i] = r
                    screen.blit(img_tama, [ta_x[i], ta_y[i]]) # 描画
                else:
                    t = 0
            elif t == 2:
                t = 0

def tama_2():
    global ta_2_x, ta_2_y, TA_2_KAZU, ta_utsu
    global idx, screen
    t = 0
    for i in range(TA_2_KAZU):
        if ta_2_y[i] != -100: # 有効なら
            ta_2_y[i] = ta_2_y[i] - TA_SPD # 弾を動かす
            if ta_2_y[i] < -80: # 画面外なら
                ta_2_y[i] = -100 # 無効化
            else:
#                dx = abs((ch_x+75) - (ta_x[i]+15))
#                dy = abs((ch_y+75) - (ta_y[i]+60))
#                if dx <= ATARIHANTEI_X and dy <= ATARIHANTEI_Y:
#                    gmov = i
#                    idx = 2
                screen.blit(img_tama_2, [ta_2_x[i], ta_2_y[i]]) # 描画
        else:   
            if t == 0:
                if ta_utsu == 1: # Zが押されたなら
                    t = 1
                    ta_2_y[i] = ch_y
                    ta_2_x[i] = ch_x + 60
                    screen.blit(img_tama_2, [ta_2_x[i], ta_2_y[i]]) # 描画

def main():
    global tmr, idx, screen
    global ch_x, ch_y, CH_SPD
    global TA_MAX, ta_x, ta_y, ka_kazu, TA_SPD, ta_kakuritsu
    global ta_2_x, ta_2_y, TA_2_KAZU, ta_utsu
    global gmov, msbx, ATARIHANTEI_X, ATARIHANTEI_Y
    pygame.init() # 初期化
    pygame.display.set_caption("シューティング") # Windowのタイトル
    clock = pygame.time.Clock() # clockオブジェクト
    while True:
        tmr = tmr + 1 # タイマー進める
        event()
        if idx == 0: # 初期化
            gmov = 0
            idx = 1
            ch_x = 565 # 主人公のX座標 初期化
            ch_y = 810 # 同じくY座標
            ta_x = [-100]*TA_MAX # 弾のX座標 初期化
            ta_y = [-100]*TA_MAX # 同じくY座標
            msbx = 0
            ta_2_x = [-100]*TA_2_KAZU # 弾のX座標 初期化 #弾2は主人公が出す弾
            ta_2_y = [-100]*TA_2_KAZU # 同じくY座標
        elif idx == 1:
            control()
            screen.blit(img_bg, [0, 0]) # 背景描画
        
            if tmr%30 < 15: # 主人公描画 15フレーム(0.5秒)ごとにアニメーション
                screen.blit(img_chara[0], [ch_x, ch_y])
            else:
                screen.blit(img_chara[1], [ch_x, ch_y])
            tama()
            tama_2()

        elif idx == 2:
            screen.blit(img_bg, [0, 0]) # 背景描画
            screen.blit(img_chara[2], [ch_x, ch_y])
            screen.blit(img_tama, [ta_x[gmov], ta_y[gmov]]) # 描画
            if msbx == 0:
                msbx = 1
            elif msbx == 1:
                msbx = 2
                messagebox.showinfo("ゲームオーバー！", "弾に当たってしまいました。スペースキーまたはエンターキーでもう一回プレイできます。")
        
        pygame.display.update()
        clock.tick(30)

if __name__ == '__main__':
    main()
