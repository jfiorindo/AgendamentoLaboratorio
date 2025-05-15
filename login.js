document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");

    form.addEventListener("submit", async function (e) {
        e.preventDefault();

        const nome = document.getElementById("nome").value;
        const senha = document.getElementById("senha").value;

        const res = await fetch("http://localhost:5000/login", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ nome, senha })
        });

        const data = await res.json();

        if (res.ok) {
            sessionStorage.setItem("usuario_id", data.usuario_id);
            window.location.href = "main.html";
        } else {
            alert(data.mensagem);
        }
    });
});
