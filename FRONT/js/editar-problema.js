const API_BASE_URL =
  (window.ENV && window.ENV.API_BASE_URL) || "http://localhost:8000/";

const rawUser = localStorage.getItem("user");
if (!rawUser) {
  window.location.href = "Connexion.html";
}

const params = new URLSearchParams(window.location.search);
const problemaId = params.get("id");

const problemIdLabel = document.getElementById("problem-id-label");
const form = document.getElementById("edit-problem-form");
const messageEl = document.getElementById("edit-message");
const cancelBtn = document.getElementById("cancel-btn");

if (!problemaId) {
  setMessage(
    "Nenhum ID de problema foi encontrado na URL (ex.: ?id=3).",
    "error"
  );
  if (problemIdLabel) {
    problemIdLabel.textContent = "";
  }
} else {
  if (problemIdLabel) {
    problemIdLabel.textContent = `#${problemaId}`;
  }
  carregarProblema(problemaId);
}

function setMessage(text, type) {
  messageEl.textContent = text || "";
  messageEl.className = "edit-message";
  if (type === "error") {
    messageEl.classList.add("edit-message--error");
  } else if (type === "success") {
    messageEl.classList.add("edit-message--success");
  }
}

async function carregarProblema(id) {
  try {
    setMessage("Carregando dados do problema...", null);

    const response = await fetch(`${API_BASE_URL}/problemas/${id}/`);

    if (!response.ok) {
      setMessage("Não foi possível carregar este problema.", "error");
      return;
    }

    const problema = await response.json();

    document.getElementById("titulo").value = problema.titulo || "";
    document.getElementById("descricao").value = problema.descricao || "";
    document.getElementById("status").value = problema.status || "";
    document.getElementById("prioridade").value = problema.prioridade || "";
    document.getElementById("origem").value = problema.origem || "";
    document.getElementById("link_relacionado").value =
      problema.link_relacionado || "";

    setMessage("", null);
  } catch (error) {
    console.error(error);
    setMessage(
      "Erro de rede ao carregar os dados. Tente novamente mais tarde.",
      "error"
    );
  }
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  if (!problemaId) return;

  const titulo = document.getElementById("titulo").value.trim();
  const descricao = document.getElementById("descricao").value.trim();
  const status = document.getElementById("status").value;
  const prioridade = document.getElementById("prioridade").value;
  const origem = document.getElementById("origem").value.trim();
  const linkRelacionado = document
    .getElementById("link_relacionado")
    .value.trim();

  if (!titulo) {
    setMessage("O campo título é obrigatório.", "error");
    return;
  }

  const payload = {
    titulo: titulo,
    descricao: descricao || null,
    status: status || null,
    prioridade: prioridade || null,
    origem: origem || null,
    link_relacionado: linkRelacionado || null
  };

  try {
    setMessage("Salvando alterações...", null);

    const response = await fetch(`${API_BASE_URL}/problemas/${problemaId}/`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(payload)
    });

    if (!response.ok) {
      setMessage("Não foi possível salvar as alterações.", "error");
      return;
    }

    const updated = await response.json();
    console.log("Problema atualizado:", updated);
    setMessage("Alterações salvas com sucesso!", "success");

  } catch (error) {
    console.error(error);
    setMessage(
      "Erro de rede ao salvar as alterações. Tente novamente.",
      "error"
    );
  }
});

cancelBtn.addEventListener("click", () => {
  window.location.href = "dashboard.html";
});
