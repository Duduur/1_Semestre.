from collections import deque


historico = deque()

historico.append("Google")
historico.append("Youtube")
historico.appendleft("Tiktok")
historico.append("Instagram")
historico.appendleft("Valorant")
historico.append("Spotify")

pagina = historico.pop()
removida = historico.popleft()



print("Historico inicial:", historico)