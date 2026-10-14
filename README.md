# Les Caillasses – Club d'escalade du Diois

Site web statique HTML/CSS/JS du club d'escalade « Les Caillasses » (Die, Drôme), reproduit à l'identique d'après l'ancien site Google Sites.

Le site est conçu pour être hébergé facilement sur **GitHub Pages** et modifiable avec de **simples fichiers texte Markdown** sans aucune dépendance logicielle complexe.

---

## 📁 Structure du projet

```text
lescaillasses.org/
├── content/                     # 📝 FICHIERS TEXTES À MODIFIER
│   ├── accueil.md               # Page d'accueil (titre, intro, cartes)
│   ├── les-cours.md             # Horaires, cours enfants/adultes, tarifs cours
│   ├── la-salle.md              # Règlement, tarifs salle, horaires, plan
│   ├── info-falaises.md         # Réglementation falaises, zones gypaètes, carte
│   ├── autres-activites.md      # Autres activités du club
│   └── historique.md            # Historique du club
│
├── assets/                      # Ressources du site
│   ├── css/style.css            # Feuille de style CSS
│   ├── js/main.js               # Menu responsive mobile et interactions
│   └── images/                  # Toutes les photos et le logo du club
│       ├── logo.png
│       ├── hero-diois.jpg
│       ├── hero-cours.jpg
│       ├── hero-salle.jpg
│       ├── hero-autres.jpg
│       ├── card-cours.jpg
│       ├── card-salle.jpg
│       ├── card-falaises.jpg
│       ├── card-autres.jpg
│       └── plan-acces-abbaye.png
│
├── templates/
│   └── base.html                # Gabarit HTML partagé (en-tête, navigation, pied de page)
│
├── build.py                     # Script Python autonome pour générer le site
│
├── index.html                   # Pages HTML statiques générées (prêtes pour le web)
├── les-cours.html
├── la-salle.html
├── info-falaises.html
├── autres-activites.html
├── historique.html
│
└── .github/workflows/deploy.yml # Déploiement automatique sur GitHub Pages
```

---

## ✏️ Comment modifier le contenu du site ?

Pour changer le texte d'une page, il suffit de modifier le fichier correspondant dans le dossier **`content/`** :

- **Page d'accueil** : [`content/accueil.md`](content/accueil.md)
- **Les cours** : [`content/les-cours.md`](content/les-cours.md)
- **La salle** : [`content/la-salle.md`](content/la-salle.md)
- **Info Falaises** : [`content/info-falaises.md`](content/info-falaises.md)
- **Autres activités** : [`content/autres-activites.md`](content/autres-activites.md)
- **Historique** : [`content/historique.md`](content/historique.md)

### Depuis l'interface web de GitHub (le plus simple) :
1. Naviguez jusqu'au fichier désiré dans le dossier `content/`.
2. Cliquez sur l'icône de crayon (✏️ *Edit this file*).
3. Modifiez le texte.
4. Cliquez sur le bouton vert **Commit changes**.
5. Grâce au workflow GitHub Actions inclus, le site se régénère et se met à jour automatiquement en ligne !

### En local sur votre ordinateur :
1. Modifiez le fichier `.md` dans votre éditeur de texte favori.
2. Ouvrez un terminal dans le dossier et lancez :
   ```bash
   python build.py
   ```
   *(ou `python3 build.py` sous Linux/macOS)*
3. Les fichiers HTML à la racine sont instantanément mis à jour.

---

## 💻 Tester le site en local

Aucune installation complexe n'est nécessaire. Vous pouvez :

- Soit faire un double-clic sur [`index.html`](index.html) pour l'ouvrir dans votre navigateur web.
- Soit lancer le serveur web intégré de Python :
  ```bash
  python -m http.server 8000
  ```
  Puis ouvrir dans votre navigateur : `http://localhost:8000`

---

## 🚀 Mise en ligne sur GitHub Pages

1. Si ce n'est pas déjà fait, configurez le dépôt distant :
   ```bash
   git remote set-url origin https://github.com/oalam/web-caillasses.git
   ```
2. Poussez les branches :
   ```bash
   git push -u origin main
   git push -u origin site-statique
   ```
3. Dans les paramètres du dépôt GitHub :
   - Allez dans **Settings** > **Pages**
   - Sous **Build and deployment > Source**, choisissez **GitHub Actions** (recommandé : le site se reconstruira automatiquement via le workflow inclus `.github/workflows/deploy.yml`).
   - *(Méthode alternative sans workflow)* : vous pouvez aussi choisir **Deploy from a branch**, puis sélectionner la branche **`main`** (ou **`site-statique`**) et le dossier **/ (root)**.
   - Le site sera en ligne à l'adresse fournie par GitHub Pages !

---

## 📄 Licence & Crédits
- Association Les Caillasses (Die).
- Photos et logo d'origine issus du club Les Caillasses.
