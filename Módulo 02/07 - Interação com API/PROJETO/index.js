async function buscarProdutos() {
  try {
    const response = await fetch("lista-produtos.json")
    const produtos = await response.json()

    const grupoDiv = document.getElementById("dell-card")
    for (const produto of produtos) {
      grupoDiv.innerHTML += `
              <div class="card" data-id="${produto.id}">
                  <img src="${produto.imagem[0]}" alt="" width="200" height="200">
                  <h2>${produto.nome}</h2>
                  <h3>${produto.descrição}</h3>
                  <div class="valores" id="valores">
                  </div>
              </div>
              `
    }

    const divsCards = document.querySelectorAll(".card")
    divsCards.forEach(card => {
      card.addEventListener("click", () => {
        const elementoId = card.getAttribute("data-id")
        window.location.href = `detalhes.html?produto-id=${elementoId}`
      })
    })
  } catch (error) {
    console.error("Erro ao buscar produtos:", error)
  }
}


buscarProdutos()