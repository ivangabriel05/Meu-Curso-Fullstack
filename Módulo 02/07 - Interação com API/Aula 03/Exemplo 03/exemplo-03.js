async function chamada(){
    let receber = await fetch("pizza.txt")
    let pagamento = await receber.text()
    console.log(pagamento)
}
chamada()