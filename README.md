# Compte rendu TP3 Python - Yoann MAHIOUT 3A32

## Réponse aux questions
#### Qu’est-ce qu’un bot ?
Un bot est un bot.

#### Qu'est ce que le logging. À quoi servent les logs?
le loggingest un truc de log. Utilisé Nottement dans le milieu des bucherons.


## Fonctionnement du Bot
Le bot va utiliser un LLM pour répondre à un prompt.
### Commandes
- `!help` : Liste de commandes supportées par le bot. 
- `!prompt <message>` :  Génère une réponse au message en utilisant Llama2.
- `!ping` : Le bot va répondre avec "Pong!"

### Ollama
[Ollama](https://ollama.com/) est un service pour faire tourner localement un LLM de notre choix, dans notre cas il s'agit de Llama2.

## Installation 

Certains prérequis sont nécessaires pour mettre en marche le bot : 

- Télécharger ollama: [https://ollama.com/](https://ollama.com/)
- Lancer Llama2 avec :  `ollama run llama2`

Ensuite :<br> 
`curl https://ollama.ai/install.sh | sh`<br>
`ollama serve`

installez les dépendances pythons : <br>
`pip install -r requirements.txt`

Enfin, renseignez le token du bot dans **config.json**

## Lancement 
Lancez le bot avec la commande : 
`python3 bot.py -c config.json`