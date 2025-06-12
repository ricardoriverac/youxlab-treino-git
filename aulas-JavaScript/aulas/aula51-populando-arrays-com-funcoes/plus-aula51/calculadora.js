function apagar() {
  const input1 = [...document.getElementsByClassName("input")];
  console.log(input1);
  input1.map((e, i) => {
    e.value = "";
  });
}

// botao somar
function somar() {
  let valor1 = parseFloat(document.getElementById("valor1").value);
  let valor2 = parseFloat(document.getElementById("valor2").value);

  let resultado = document.getElementById("resultado");

  resultado.value = valor1 + valor2;
}

// botao subtrair
function subtrair() {
  let valor1 = parseFloat(document.getElementById("valor1").value);
  let valor2 = parseFloat(document.getElementById("valor2").value);

  let resultado = document.getElementById("resultado");

  resultado.value = valor1 - valor2;
}

// botao multiplicar
function multiplicar() {
  let valor1 = parseFloat(document.getElementById("valor1").value);
  let valor2 = parseFloat(document.getElementById("valor2").value);

  let resultado = document.getElementById("resultado");

  resultado.value = valor1 * valor2;
}

// botao dividir
function dividir() {
  let valor1 = parseFloat(document.getElementById("valor1").value);
  let valor2 = parseFloat(document.getElementById("valor2").value);

  let resultado = document.getElementById("resultado");

  resultado.value = valor1 / valor2;
}
