#!/bin/bash

# 🌌 Script magique pour commit + push

echo "🔍 Étape 1 : Ajout des fichiers..."
git add .

echo "📝 Étape 2 : Écriture du commit..."
git commit -m "🔄 Mise à jour automatique – OpenSpace ePlanet"

echo "🚀 Étape 3 : Envoi vers GitHub..."
git push

echo "✅ Fichiers gravés dans le ciel de GitHub."
chmod +x commit-and-push.sh

#!/bin/bash

echo "📦 Étape 1 : Ajout des fichiers..."
git add .

echo "📝 Étape 2 : Création du commit..."
git commit -m "🔄 Mise à jour automatique – $(date '+%Y-%m-%d %H:%M:%S')"

echo "🚀 Étape 3 : Envoi vers GitHub..."
git push

echo "✅ Terminé : tous les fichiers sont sur GitHub !"

