import board
import busio
import pokecon

uart = busio.UART(tx=board.GP0, rx=board.GP1, baudrate=9600, bits=8, parity=None, stop=1, timeout=0.1, receiver_buffer_size=64)
pc_report_str = ""

while True:
    pc_report_str = uart.readline()
    if pc_report_str is not None:
        pokecon.parseline(pc_report_str.decode('utf-8'))
        pc_report_str = ""
        pokecon.ProgState = pokecon.LoopState.STATE1

    if pokecon.ProgState == pokecon.LoopState.STATE1:
        pokecon.switch_funtion()
    else:
        pokecon.ProgState = pokecon.LoopState.STATE0
