import pygame
import sys
import time

pygame.init()

# --------------------------------
# 기본 설정
# --------------------------------
WIDTH, HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PPT EVENT 15~34 FINAL")

CLOCK = pygame.time.Clock()
FPS = 60

WHITE = (255,255,255)
BLACK = (0,0,0)
RED   = (220,50,50)

FONT = pygame.font.Font("DOSGothic.ttf", 26)
BIG_FONT = pygame.font.Font("DOSGothic.ttf", 120)

# 타자기 속도 (클수록 빠름)
TEXT_SPEED = 2

# 타자기 상태
current_text = ""
full_text = ""
text_index = 0
typing_done = False


# --------------------------------
# 공용 함수
# --------------------------------
def load_bg(path):
    return pygame.transform.scale(
        pygame.image.load(path).convert_alpha(), (WIDTH, HEIGHT)
    )


# --------------------------------
# 이미지 로드
# --------------------------------
table_bg   = load_bg("table_selection1.png")
room_bg    = load_bg("room.png")
keyhole_bg = load_bg("key hole_background.png")
hallway_bg = load_bg("hallway_background.png")
gameover_bg = load_bg("gameover_background.png")

key_img = pygame.transform.scale(pygame.image.load("key_selection1.png"), (150,150))
cup_img = pygame.transform.scale(pygame.image.load("cup_selection1.png"), (170,170))
notebook_img = pygame.transform.scale(pygame.image.load("notebook_selection1.png"), (170,170))
handkerchief_img = pygame.transform.scale(pygame.image.load("handkerchief_selection1.png"), (170,170))

cup_rect      = cup_img.get_rect(center=(320,360))
notebook_rect = notebook_img.get_rect(center=(640,360))
handker_rect  = handkerchief_img.get_rect(center=(960,360))
key_rect      = key_img.get_rect(center=(640,200))

# KEY HOLE KEY
keyhole_raw = pygame.image.load("key hole_key.png").convert_alpha()
KH = 150
ratio = KH / keyhole_raw.get_height()
KW = int(keyhole_raw.get_width() * ratio)
keyhole_key_img = pygame.transform.scale(keyhole_raw, (KW, KH))

# BLOOD (화면 전체 덮는 피 이미지)
blood_img = pygame.transform.scale(
    pygame.image.load("blood.png").convert_alpha(), (WIDTH, HEIGHT)
)

# 선택창 이미지
select_box = pygame.transform.scale(
    pygame.image.load("selection box.png").convert_alpha(), (400,120)
)
select_rect = select_box.get_rect(center=(640,610))


def draw_select_text(text):
    txt = FONT.render(text, True, (0,0,0))
    SCREEN.blit(txt, txt.get_rect(center=select_rect.center))


# 대사창
dialogue_box = pygame.transform.scale(
    pygame.image.load("chatbox.png").convert_alpha(), (1280,200)
)


# --------------------------------
# 캐릭터 이미지
# --------------------------------
elen_raw = pygame.image.load("Elenore.png").convert_alpha()
EH = 620
ratio = EH / elen_raw.get_height()
EW = int(elen_raw.get_width() * ratio)
elen_img = pygame.transform.scale(elen_raw, (EW, EH))
ELEN_POS = (-200, HEIGHT - EH)

# 왕 이미지 (엘레노어의 55%)
KING_SCALE = 0.55
KING_W = int(EW * KING_SCALE)
KING_H = int(EH * KING_SCALE)

king_raw = pygame.image.load("king.png").convert_alpha()
king_img = pygame.transform.smoothscale(king_raw, (KING_W, KING_H))

KING_OFFSET_X = 100
KING_POS = (ELEN_POS[0] + KING_OFFSET_X, HEIGHT - KING_H)


# --------------------------------
# 열쇠 이동
# --------------------------------
key_start    = pygame.Vector2(640,200)
key_hole_pos = pygame.Vector2(440,300)
key_pos      = key_start.copy()
key_anim     = False


# --------------------------------
# 씬 & 대사
# --------------------------------
scene = 15
fade_done = False

dialogues = {
    21: ["???: 덜컥, 끼이--익....."],
    22: ["“뭐지.. 문이 이렇게 쉽게 열리다니.”", "한 번 문을 열고 나가보자."],
    23: [
        "문을 열자 보이는 것은 매우 넓은 복도였다.",
        "앞의 문에 정신이 팔려 이제 되었다는 안도감과 벅차오름에",
        "잠시 멍을 때리고 있었다."
    ],
    24: ["???: 터벅-, 터벅-"],
    25: ["???: 휙- 탁!, 푹- (칼로 찌르는 소리)"],
    26: [
        "등에서 따듯한 느낌과 함께 무언가 흘러내린다.",
        "내 피인건가 장기인건가...",
        "뒤를 돌아보자 왕이 내 뒤에 서 있다.",
        "그럼 지금까지 내가 나오길 기다린건가?",
        "나를 시험한건가?"
    ],
    27: [
        "“내 딸과 같은 엘레노어, 넌 늘 똑똑한 아이였지.",
        "그래서 내가 널 내 아들 제프리와 결혼시키려 한거란다.",
        "하지만 엘레노어, 네가 이렇게까지 결혼하기 싫어한다면",
        "이후에 결혼을 억지로 해도 날 끝까지 원망하겠지.",
        "하지만 난 그런 자에게 내 나라의 국모를 맡기기 싫단다.",
        "이후 나이 든 나를 어떻게 대할진 뻔하지 않은가?”"
    ],
    28: [
        "“그러니 너무 원망하지 말게, 너의 집안을 대체할 사업체는 많다네 엘레노어.",
        "지금쯤이면 내가 보낸 사람에 의해 네 사랑 윌리엄도 죽었을거네.",
        "웃기지 않은가? 자기가 사랑하는 여자 하나 못지키다니.",
        "둘이 함께 하늘에서 평안하길 비네 엘레노어.",
        "이 말은 진심이니 너무 꼬아듣지 말길 바라네.”"
    ],
    29: ["“Knights, to me!, 이 여자 들고가서 태워!", "그리고~....”"],
    30: [
        "오만 생각이 들었지만 내가 생각을 할 땐 모두 늦어 있었다.",
        "이제 진짜 끝이구나...",
        "아... 윌리엄...",
        "이젠 우리 둘 다 끝이구나..."
    ]
}

dialogue_18 = ["좋아, 이 열쇠… 여기에 맞을지도 몰라."]


# --------------------------------
# 타자기 효과
# --------------------------------
def start_typing(lines):
    """여러 줄 대사를 타자기 효과로 준비"""
    global full_text, current_text, text_index, typing_done
    full_text = "\n".join(lines)
    current_text = ""
    text_index = 0
    typing_done = False

def update_typing():
    """1프레임에 몇 글자씩 출력"""
    global full_text, current_text, text_index, typing_done

    if typing_done:
        return
    
    for _ in range(TEXT_SPEED):
        if text_index < len(full_text):
            current_text += full_text[text_index]
            text_index += 1
        else:
            typing_done = True
            break


# --------------------------------
# 캐릭터 등장 여부
# --------------------------------
def character_present(scene):
    if scene == 18:
        return "elenore"
    if 27 <= scene <= 29:
        return "king"
    return None


# --------------------------------
# 대사창 + 타자기 출력
# --------------------------------
def draw_typing_text(scene):
    SCREEN.blit(dialogue_box, (0, HEIGHT - 200))

    char = character_present(scene)
    color = RED if 24 <= scene <= 29 else WHITE
    x = 260 if char is None else 380
    y = HEIGHT - 160

    lines = current_text.split("\n")

    for i, line in enumerate(lines):
        if 24 <= scene <= 29:
            # Bold 빨간
            t1 = FONT.render(line, True, color)
            t2 = FONT.render(line, True, color)
            SCREEN.blit(t1, (x, y + i*32))
            SCREEN.blit(t2, (x+2, y + i*32))
        else:
            t = FONT.render(line, True, color)
            SCREEN.blit(t, (x, y + i*32))


# --------------------------------
# 페이드 아웃
# --------------------------------
def fade_out():
    fade = pygame.Surface((WIDTH,HEIGHT))
    fade.fill(BLACK)
    for a in range(0,255,25):
        fade.set_alpha(a)
        draw_scene()
        SCREEN.blit(fade,(0,0))
        pygame.display.flip()
        CLOCK.tick(FPS)


# --------------------------------
# 장면 렌더링
# --------------------------------
def draw_scene():
    global key_pos

    # ----- 15 -----
    if scene == 15:
        SCREEN.blit(table_bg,(0,0))
        SCREEN.blit(cup_img,cup_rect)
        SCREEN.blit(notebook_img,notebook_rect)
        SCREEN.blit(handkerchief_img,handker_rect)
        SCREEN.blit(key_img,key_rect)

    # ----- 16 -----
    elif scene == 16:
        SCREEN.blit(table_bg,(0,0))
        SCREEN.blit(cup_img,cup_rect)
        SCREEN.blit(notebook_img,notebook_rect)
        SCREEN.blit(handkerchief_img,handker_rect)

        dark = pygame.Surface((WIDTH,HEIGHT), pygame.SRCALPHA)
        dark.fill((0,0,0,180))
        SCREEN.blit(dark,(0,0))

        SCREEN.blit(key_img,key_rect)

    # ----- 17 -----
    elif scene == 17:
        SCREEN.blit(table_bg,(0,0))
        SCREEN.blit(cup_img,cup_rect)
        SCREEN.blit(notebook_img,notebook_rect)
        SCREEN.blit(handkerchief_img,handker_rect)

        dark = pygame.Surface((WIDTH,HEIGHT), pygame.SRCALPHA)
        dark.fill((0,0,0,180))
        SCREEN.blit(dark,(0,0))

        SCREEN.blit(key_img,key_rect)
        SCREEN.blit(select_box,select_rect)
        draw_select_text("열쇠를 집는다")

    # ----- 18 -----
    elif scene == 18:
        SCREEN.blit(room_bg,(0,0))
        draw_typing_text(scene)
        SCREEN.blit(elen_img, ELEN_POS)

    # ----- 19 -----
    elif scene == 19:
        SCREEN.blit(keyhole_bg,(0,0))
        SCREEN.blit(keyhole_key_img, keyhole_key_img.get_rect(center=key_pos))
        SCREEN.blit(select_box,select_rect)
        draw_select_text("열쇠를 사용한다")

    # ----- 20 -----
    elif scene == 20:
        SCREEN.blit(keyhole_bg,(0,0))
        SCREEN.blit(keyhole_key_img, keyhole_key_img.get_rect(center=key_pos))

    # ----- 21 ~ 30 -----
    elif 21 <= scene <= 30:
        SCREEN.blit(hallway_bg,(0,0))
        draw_typing_text(scene)

        if 27 <= scene <= 29:
            SCREEN.blit(king_img, KING_POS)

        if 24 <= scene <= 29:
            SCREEN.blit(blood_img,(0,0))

    # ----- 31 -----
    elif scene == 31:
        SCREEN.blit(gameover_bg,(0,0))

    elif scene == 32:
        SCREEN.blit(gameover_bg,(0,0))

        # GAME OVER 크게
        t1 = BIG_FONT.render("GAME OVER", True, RED)
        t2 = BIG_FONT.render("GAME OVER", True, RED)

        x = 640 - t1.get_width()//2
        y = 150

        SCREEN.blit(t1, (x,y))
        SCREEN.blit(t2, (x+4,y))

        # 아래 문장
        last = FONT.render("사랑도 권력 앞에선 우습나봅니다...", True, WHITE)
        SCREEN.blit(last, (640-last.get_width()//2, y+180))

        # 선택창
        SCREEN.blit(select_box, select_rect)

        # 선택창 글씨
        txt = FONT.render("다시 진행", True, (0,0,0))
        SCREEN.blit(txt, txt.get_rect(center=select_rect.center))


# --------------------------------
# 업데이트
# --------------------------------
def update():
    global scene, key_anim, key_pos, fade_done

    update_typing()

    if scene == 20 and key_anim:
        key_pos += (key_hole_pos - key_pos) * 0.2
        if key_pos.distance_to(key_hole_pos) < 5:
            key_pos = key_hole_pos.copy()
            key_anim = False
            fade_out()
            scene = 21
            start_typing(dialogues[21])

    if scene == 31 and not fade_done:
        fade = pygame.Surface((WIDTH,HEIGHT))
        fade.fill(BLACK)
        for a in range(0,255,20):
            fade.set_alpha(255 - a)
            SCREEN.blit(gameover_bg,(0,0))
            SCREEN.blit(fade,(0,0))
            pygame.display.flip()
            CLOCK.tick(60)

        fade_done = True
        scene = 32



# --------------------------------
# 입력 처리
# --------------------------------
def handle_input():
    global scene, key_anim, key_pos

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if scene == 15:
                fade_out()
                scene = 16

            elif scene == 16:
                scene = 17

            elif scene == 17 and select_rect.collidepoint(event.pos):
                fade_out()
                scene = 18
                start_typing(dialogue_18)

            elif scene == 18:
                scene = 19

            elif scene == 19 and select_rect.collidepoint(event.pos):
                fade_out()
                scene = 20
                key_anim = True
                key_pos = key_start.copy()

            elif 21 <= scene <= 30:
                scene += 1

                # 21 ~ 30만 대사 있음
                if scene <= 30:
                    start_typing(dialogues[scene])

            elif scene == 31:
                pass

            elif scene == 32:
                pass



# --------------------------------
# 메인 루프
# --------------------------------
while True:
    CLOCK.tick(FPS)
    handle_input()
    update()

    SCREEN.fill(BLACK)
    draw_scene()
    pygame.display.flip()
