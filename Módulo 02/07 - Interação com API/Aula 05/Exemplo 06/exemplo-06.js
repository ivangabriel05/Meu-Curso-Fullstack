async function concessionaria(){
    let resultado = await fetch("carros,json")
    let carros = await resultado.json()
//alert("A marca é " + carros.marca + ", O modelo é " + carros.modelo + " o ano é " + carros.ano + " e a cor é " + carros.cor + "." )
//alert("carros[1].modelo")

document.body.innerHTML += `
    <h1>A marca do carro é ${carros[1].marca}</h1>
    <h2>O modelo é ${carros[1].modelo}</h2>
    <h3>O ano é ${carros[1].ano}</h3>
    <h4>A cor é ${carros[1].cor}</h4>  
`

}
concessionaria()