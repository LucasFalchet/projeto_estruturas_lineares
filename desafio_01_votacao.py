import subprocess

subprocess.run("cls",shell=True)

votos = []

while True:
    voto = input("Digite o nome do candidato (Ana, Bruno ou Carlos) ou 'fim' para encerrar: ").strip().lower()
    
    if voto == "fim":
        break
    
    if voto in ["ana", "bruno", "carlos"]:
        votos.append(voto)
    else:
        print("Candidato inválido! Tente novamente.")

votos_ana = votos.count("ana")
votos_bruno = votos.count("bruno")
votos_carlos = votos.count("carlos")

subprocess.run("cls",shell=True)

print("Resultado da votação:")
print(f"Ana: {votos_ana} votos\nBruno {votos_bruno} votos\nCarlos {votos_carlos} votos")

if votos_ana > votos_bruno and votos_carlos:
    print("O vencedor é: Ana.")
elif votos_bruno > votos_ana and votos_carlos:
    print("O vencedor é: Bruno.")
elif votos_carlos > votos_ana and votos_bruno:
    print("O vencedor é: Carlos.")
else:
    print("Houve um empate entre os candidatos.")