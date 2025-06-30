#!/bin/bash

echo "🌟 Début de la restructuration du projet Vite..."

# Se placer dans le bon dossier
cd html5up-hyperspace/vite-project || { echo "❌ Dossier vite-project introuvable."; exit 1; }

echo "📦 Déplacement des fichiers vers la racine du dépôt..."

# Déplacer les fichiers visibles
mv * ../.. || echo "❌ Erreur lors du déplacement des fichiers visibles."

# Déplacer les fichiers cachés (.env, .gitignore, etc.)
mv .[^.]* ../.. 2>/dev/null || echo "⚠️ Aucun fichier caché trouvé ou déjà déplacé."

cd ../..

# Supprimer l'ancien dossier vite-project s’il est vide
rmdir html5up-hyperspace/vite-project 2>/dev/null && echo "🧹 Dossier vite-project supprimé." || echo "⚠️ Impossible de supprimer vite-project (non vide ou inexistant)."

# Ajouter tous les changements
git add .

# Commit clair et lyrique
git commit -m "🌈 Réorganisation – projet Vite remonté à la racine pour Vercel"

# Push for
