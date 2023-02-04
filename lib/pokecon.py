import usb_hid
import struct
from switchcontroller import SwitchController, Hat, Stick


class ProcState:
    NONE                     = 0x00 # do nothing
    # On MCU
    DEBUG                    = 0x0a
    DEBUG2                   = 0x0b

    # From PC
    PC_CALL                  = 0x0c


class LoopState:
    STATE0 = 0  # シリアル通信受信→受信成功
    STATE1 = 1  # シリアル通信成功時
    STATE2 = 2  # 判定


button = 0
hat = Hat.CENTER
lx = Stick.CENTER
ly = Stick.CENTER
rx = Stick.CENTER
ry = Stick.CENTER
dummy = 0
ProgState = 0
proc_state = 0

sc = SwitchController(usb_hid.devices)
sc.reset_all()

def sendreport():
    global report,button,hat,lx,ly,rx,ry,dummy
    report = struct.pack(
        "<HBBBBBb",
        button,
        hat,
        lx,
        ly,
        rx,
        ry,
        dummy
        )
    sc.sendreport(report)


def parseline(string):
    global proc_state
    global ProgState
    global button,hat,lx,ly,rx,ry
    cmd = str(string)
    #print("cmd="+cmd)

    if cmd.startswith('end'):
        proc_state = ProcState.NONE
        sc.reset_all()
    elif (cmd[0] >= '0') and (cmd[0] <= '9'):
        buf = cmd.split(' ')
        p_btns = 0
        p_hat  = Hat.CENTER
        pc_lx  = Stick.CENTER
        pc_ly  = Stick.CENTER
        pc_rx  = Stick.CENTER
        pc_ry  = Stick.CENTER
        if len(buf) == 2: #
            p_btns = int(buf[0], 0)
            p_hat  = int(buf[1])
        elif len(buf) == 4:
            p_btns = int(buf[0])
            p_hat  = int(buf[1])
            pc_lx  = int(buf[2], 16)
            pc_ly  = int(buf[3], 16)

        elif len(buf) == 6:
            p_btns = int(buf[0])
            p_hat  = int(buf[1])
            pc_lx  = int(buf[2], 16)
            pc_ly  = int(buf[3], 16)
            pc_rx  = int(buf[4], 16)
            pc_ry  = int(buf[5], 16)

        # HAT : 0(TOP) to 7(TOP_LEFT) in clockwise | 8(CENTER)
        hat = p_hat

        # we use bit array for buttons(2 Bytes), which last 2 bits are flags of directions
        use_right = bool(p_btns & 0x0001)
        use_left  = bool(p_btns & 0x0002)

        # Left stick
        if (use_left):
            lx = pc_lx
            ly = pc_ly

        # Right stick
        if (use_right & use_left):
            rx = pc_rx
            ry = pc_ry
        elif (use_right):
            rx = pc_lx
            ry = pc_ly

        p_btns >>= 2
        button = p_btns

        proc_state = ProcState.PC_CALL

    else:
        proc_state = ProcState.DEBUG2


def switch_funtion():
    global ProgState

    if proc_state == ProcState.PC_CALL:
        sendreport();  #解析したデータをSwitchに送信
        ProgState = LoopState.STATE0
    else:
        pass