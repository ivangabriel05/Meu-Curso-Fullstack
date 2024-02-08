async function buscar(){
    let resposta = await fetch("msg.txt")
    let convertido = await resposta.text()
    //console.log(lista)
    let lista = ["manga", "uva", "pera"]
    for(let x in lista){
        document.body.innerHTML += `
            <h1>
                ${convertido} 
            </h1>
            <p>
                ${x}
            </p>
        `
        
    } 
}

buscar()