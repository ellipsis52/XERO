app.get('/messages', async (req, res) => {
    const key = req.headers['x-api-key'];
    if (key !== process.env.API_SECRET_KEY) return res.status(403).send("⛔ Accès refusé");
  
    const messages = await prisma.message.findMany({
      include: { client: true },
      orderBy: { createdAt: 'desc' },
    });
  
    res.json(messages);
  });
  