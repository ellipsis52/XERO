router.get('/all', async (req, res) => {
    const messages = await prisma.message.findMany({
      orderBy: { createdAt: 'desc' },
    });
    res.json(messages);
  });
  
  router.put('/:id', async (req, res) => {
    const { prompt } = req.body;
    const updated = await prisma.message.update({
      where: { id: req.params.id },
      data: { prompt },
    });
    res.json(updated);
  });

  