import nmap

scanner = nmap.PortScanner()

print("Seja Bem-vindo ao Scanner Port")
print("<----------------------------->")

ip = input("Digite o ip a ser verificado: ")
print("O ip digitado foi: ", ip)
type(ip)

menu = input(""""\n Escolha o tipo de varredura a ser realizada
    1 => Varredurado tipo SYB
    2 => Varredura do tipo UDP
    3 => Varredura do tipo INTENSA
    Digite a opção escolhida: """)
print("A opção escolhida foi ", menu)

if menu == "1":
    print("Versão do Nmap: ", scanner.nmap_version())
    scanner.scan(ip, "1 - 1024", "-v -sS")
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("Portas abertas: ", scanner[ip]['tcp'].keys())
elif menu == "2":
    print("Versão no Nmap: ", scanner.nmap_version())
    scanner.scan(ip, '1 - 1024', '-v -sU')
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("Portas abertas: ", scanner[ip]['udp'].keys())
elif menu == "3":
    print("Versão no Nmap: ", scanner.nmap_version())
    scanner.scan(ip, '1 - 1024', '-v -sC')
    print(scanner.scaninfo())
    print("Status do IP: ", scanner[ip].state())
    print(scanner[ip].all_protocols())
    print("")
    print("Portas abertas: ", scanner[ip]['udp'].keys())

else:
    print("Escolha corretamente de 1 ao 3")