async function obter( ){
    let resposta = await fetch("maça.txt")
    let convertido = await resposta.text()
    console.log(convertido)
}
obter()