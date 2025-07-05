#!/bin/bash

set -e  # Arrêter le script en cas d’erreur
echo "🌐 Préparation du déploiement Vercel..."

# 1. Vérifie si vercel CLI est installé
if ! command -v vercel &> /dev/null; then
  echo "⚠️ Vercel CLI non installé. Installation en cours..."
  npm install -g vercel
fi

# 2. Lier au projet Vercel (si pas encore fait)
echo "🔗 Lien avec le projet distant..."
vercel link --yes || true

# 3. Récupère les variables d’environnement (si définies)
echo "🔑 Synchronisation des variables d'environnement..."
vercel pull --yes --environment=preview

# 4. Déploiement
echo "🚀 Lancement du déploiement vers la production..."
vercel --prod

echo "✅ Déploiement terminé avec succès ✨"
