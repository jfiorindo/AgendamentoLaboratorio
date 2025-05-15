document.addEventListener("DOMContentLoaded", function () {
    const botoes = document.querySelectorAll(".visitar-btn");

    botoes.forEach(botao => {
        botao.addEventListener("click", () => {
            const labNumero = botao.getAttribute("data-lab");
            if (labNumero) {
                // Redireciona para a página do laboratório correspondente
                window.location.href = `../PagesLab/lab${labNumero}.html`;
            }
        });
    });
});
