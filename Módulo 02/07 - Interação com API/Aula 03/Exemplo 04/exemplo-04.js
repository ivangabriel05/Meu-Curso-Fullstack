async function quero(){
    let meu = await fetch("sorte de merda.txt")
    let pagamento = await meu.text()
    console.log(pagamento)
}
quero()