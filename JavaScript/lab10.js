document.querySelectorAll(".available").forEach((celula) => {
    celula.addEventListener("click", async () => {
        const dia = celula.textContent;
        const usuario_id = sessionStorage.getItem("usuario_id");

        if (!usuario_id) {
            alert("Faça login para agendar.");
            return;
        }

        const dataFormatada = `2025-05-${dia.padStart(2, '0')}`;
        const nomeLaboratorio = "Laboratório 10"; // <-- altere conforme a página

        const res = await fetch("http://localhost:5000/agendar", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                usuario_id: usuario_id,
                laboratorio: nomeLaboratorio,
                data: dataFormatada
            })
        });

        const resultado = await res.json();
        alert(resultado.mensagem);
        celula.classList.remove("available");
        celula.classList.add("unavailable");
    });
});
