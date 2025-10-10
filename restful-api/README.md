# 📘 Documentation API — Requêtes HTTP

## 🌐 HTTP vs HTTPS  
Le **HTTP** (*HyperText Transfer Protocol*) est le protocole standard utilisé pour échanger des données entre un client (comme un navigateur ou une application) et un serveur web.  
Il fonctionne généralement sur le **port 80**.

Le **HTTPS** (*HTTP Secure*) est la version sécurisée de HTTP.  
Il ajoute une couche de chiffrement (SSL/TLS) qui protège les données échangées.  
Cette sécurité est indispensable pour les sites manipulant des informations sensibles : identifiants, données personnelles ou bancaires.  
HTTPS utilise le **port 443**.

🔓 **HTTP** → données en clair  
🔐 **HTTPS** → données chiffrées et sécurisées

---

## 🧭 Les principales méthodes HTTP

| Méthode | Rôle | Exemple d’utilisation |
|----------|------|------------------------|
| **GET** | Récupérer une ressource | Charger une page ou obtenir une liste de données. |
| **POST** | Envoyer des données au serveur | Soumettre un formulaire ou ajouter un nouvel utilisateur. |
| **PUT** | Mettre à jour ou remplacer complètement une ressource | Modifier un profil ou remplacer une entrée. |
| **DELETE** | Supprimer une ressource | Supprimer un compte utilisateur ou un élément d’une base. |

---

## 🚦 Les codes d’état HTTP les plus courants

| Code | Signification | Description |
|------|----------------|-------------|
| **200 OK** | Succès | La requête s’est déroulée correctement et le serveur renvoie la ressource demandée. |
| **400 Bad Request** | Mauvaise requête | Les données envoyées sont incomplètes ou mal formées. |
| **401 – Unauthorized** | Non authentifié | Aucune ou mauvaise authentification fournie. |
| **403 Forbidden** | Accès refusé | L’utilisateur n’a pas les autorisations nécessaires pour accéder à la ressource. |
| **404 Not Found** | Ressource introuvable | L’URL demandée n’existe pas sur le serveur. |
| **500 Internal Server Error** | Erreur interne du serveur | Une erreur s’est produite côté serveur. |

---

## 💡 En bref  
Les requêtes HTTP sont la base de toute interaction entre un client et un serveur.  
Comprendre les **méthodes** et les **codes d’état** permet de mieux concevoir, déboguer et sécuriser une API.  

---
