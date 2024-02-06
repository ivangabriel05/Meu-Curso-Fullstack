//fetch() = serve para fazer buscas no banco de dados.
//await = espera o comando ser execurtado para pode seguir o proximo comando e so funcionar dentro de uma função asincrona.
//async = serve para derfinir que ela e uma função asincrona.
// = atribuição //== comparação

async function procurar(){
    let resposta = await fetch("maça.txt")
    let convertido = await resposta.text()
    console.log(convertido)
    alert(convertido)
}
procurar()