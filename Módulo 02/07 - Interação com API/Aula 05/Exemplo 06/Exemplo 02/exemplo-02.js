async function buscar(){
    let aparelhos = await fetch("celular.json")
    let celurares = await aparelhos.json()

    for(let x in celurares){

        document.body.innerHTML += `
        <p> ${celurares[x].marca}</p>
        <p>${celurares[x].nome}</p>
        <p>${celurares[x].geracao}</p>
        <p>${celurares[x].cor}</p>
        <p style="backgroud-color: #000; height: 1px"></p>
    `
        
    }
    
}
buscar()