import socket

ip = input("Digite o HOST ou IP a ser verificado: ")

ports = []
count = 0

while count < 10:
    ports.append(int(input("Digite a porta a ser verificada: ")))
    count += 1
    if count == "0":
        break

for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.05)
    code = client.connect_ex((ip, port))

    if code == 0:
        print(str(port), "=> Porta ABERTA")
    else:
        print(str(port), "=> Porta FECHADA")

print("Scan finalizado")