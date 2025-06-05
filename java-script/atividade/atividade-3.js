const produtos = [
  { nome: "Arroz", categoria: "Alimentos", quantidade: 10 },
  { nome: "Feijão", categoria: "Alimentos", quantidade: 5 },
  { nome: "Detergente", categoria: "Limpeza", quantidade: 3 },
  { nome: "Sabão", categoria: "Limpeza", quantidade: 4 },
  { nome: "Refrigerante", categoria: "Bebidas", quantidade: 6 },
  { nome: "Suco", categoria: "Bebidas", quantidade: 8 },
];

const agrupadosPorCategoria = [];

for (const produto of produtos) {
  const { categoria, nome, quantidade } = produto;

  let grupo = agrupadosPorCategoria.find(g => g.categoria === categoria);

  if (!grupo) {

    grupo = {
      categoria,
      produtos: [],
      totalQuantidade: 0
    };
    agrupadosPorCategoria.push(grupo);
  }

  grupo.produtos.push({ nome, quantidade });
  grupo.totalQuantidade += quantidade;
}

for (const grupo of agrupadosPorCategoria) {
  console.log(`📦 Categoria: ${grupo.categoria}`);

  for (const item of grupo.produtos) {
    console.log(`  - ${item.nome}: ${item.quantidade}`);
  }

  console.log(`  🔢 Total: ${grupo.totalQuantidade}\n`);
}
