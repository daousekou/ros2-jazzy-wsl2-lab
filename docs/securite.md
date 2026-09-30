# Securite et nettoyage avant publication

Ce depot est concu pour etre publiable sans information sensible.

## Informations interdites

Ne jamais publier :

- tokens GitHub, cles API ou secrets cloud ;
- mots de passe, identifiants ou cookies ;
- fichiers `.env` reels ;
- cles SSH, certificats ou fichiers de configuration personnels ;
- chemins locaux contenant un nom d'utilisateur ;
- emails personnels ;
- URLs privees ;
- IP internes, hostnames internes ou noms de machines ;
- informations internes d'un employeur ou d'un client.

## Bonnes pratiques

- Remplacer les chemins personnels par des chemins generiques comme `~/ros2_ws`.
- Remplacer les hostnames par `localhost` ou `example.local`.
- Remplacer les IP privees par des exemples documentaires comme `192.0.2.10`.
- Ne publier que des commandes reproductibles.
- Garder les fichiers de configuration sensibles hors du depot.

## Verification simple

Avant publication :

```bash
git status
git diff --cached
```

Recherche de mots sensibles :

```bash
grep -RInE "token|password|passwd|secret|api[_-]?key|credential|email|@|C:\\\\Users|/home/" .
```

Cette recherche ne remplace pas une revue manuelle.
