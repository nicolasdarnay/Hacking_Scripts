import socket

TRG_ADDRESS = input("Type the target Address: ")
TRG_PORT = input("Type the target Port Range (ex: 23-2432): ")

low_port = int(TRG_PORT.split("-")[0])
high_port = int(TRG_PORT.split("-")[1])

for port in range(low_port, high_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = s.connect_ex((TRG_ADDRESS, port))
    if status == 0:
        print("Port:", port, "is OPEN!!!")
    else:
        print("Port:", port, "is CLOSED")
    s.close()
