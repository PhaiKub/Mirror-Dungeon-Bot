from utils import *
from event import event

PATH = pth(UI_PATH, "battle")
SINS = [name for name in os.listdir(pth(PATH, "sins"))]

# sinners = ["YISANG", "FAUST" , "ISHMAEL", "RODION", "SINCLAIR", "GREGOR"]

# SINNERS = {
#     "YISANG"    : ( 351, 207, 196, 285),
#     "FAUST"     : ( 547, 207, 196, 285),
#     "DONQUIXOTE": ( 743, 207, 196, 285),
#     "RYOSHU"    : ( 939, 207, 196, 285),
#     "MEURSAULT" : (1135, 207, 196, 285),
#     "HONGLU"    : (1331, 207, 196, 285),
#     "HEATHCLIFF": ( 351, 492, 196, 285),
#     "ISHMAEL"   : ( 547, 492, 196, 285),
#     "RODION"    : ( 743, 492, 196, 285),
#     "SINCLAIR"  : ( 939, 492, 196, 285),
#     "OUTIS"     : (1135, 492, 196, 285),
#     "GREGOR"    : (1331, 492, 196, 285)
# }

# region = (399, 272, 1081, 355)
# square = (399, 330, 1081, 239)

# def select(sinners):
    

def chain(res):
    gui.moveTo(res)
    gui.mouseDown()
    x, y = res
    x += 75
    y -= 46
    while True:
        for sin in SINS:
            try:
                locateOnScreenRGBA(pth("sins", sin), region=(int(x), int(y), 137, 139), confidence=0.8, grayscale=False, path=PATH, A=True)
                gui.moveTo(x + 68, y + 200)
                break
            except gui.ImageNotFoundException:
                continue
        else:
            gui.moveTo(x + 68, y + 70)
        
        if check("gear2.png", region=(int(x + 68 + 63), int(y + 70 - 31), 171, 183), skip_wait=True, conf=0.8, path=PATH, A=True):
            gui.press("enter", 1, 0.1)
            gui.mouseUp()
            return
        
        x += 115


def fight():
    if not check("TOBATTLE.png", region=(1586, 820, 254, 118), click=True, skip_wait=True, path=PATH) and \
       not check("battleEGO.png", region=(1525, 104, 86, 81), skip_wait=True, path=PATH): return False

    print("Entered Battle")

    while check("loading.png", region=(1577, 408, 302, 91), wait=2): # dangerous code
            print("loading screen...")
            time.sleep(0.5)


    while True:
        if check("battleEGO.png", region=(1525, 104, 86, 81), wait=1, path=PATH):
            gui.click(500, 83, duration=0.1)

            try:
                res = gui.center(locateOnScreenEdges("gear.png", region=(0, 761, 548, 179), confidence=0.5, path=f"{UI_PATH}battle/"))
                chain(res)
            except gui.ImageNotFoundException:
                gui.press("p", 1, 0.1)
                gui.press("enter", 1, 0.1)

        if check(pth("event", "eventskip.png"), region=(850, 437, 103, 52), skip_wait=True):
            event()

        if check('loading.png', region=(1577, 408, 302, 91), skip_wait=True)  or \
           check(pth("path", "Move.png"), region=(1805, 107, 84, 86), skip_wait=True) or \
           check(pth("grab", "EGObin.png"), region=(69, 31, 123, 120), skip_wait=True)       or \
           check(pth("grab", "encounterreward.png"), region=(412, 165, 771, 72), skip_wait=True):
            
            while check('loading.png', region=(1577, 408, 302, 91), skip_wait=True): # dangerous code
                time.sleep(0.1)
    
            print("Battle is over")
            logging.info("Battle is over")

            return True
        
        if gui.getActiveWindowTitle() != 'LimbusCompany':
            pause()
        
        if check('pause.png', region=(1724, 16, 83, 84), skip_wait=True, path=PATH):
            time.sleep(1)
        else:
            time.sleep(0.2)