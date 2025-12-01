const API_BASE_URL = "http://localhost:8000/api";

const form = document.getElementById("login-form");
const messageEl = document.getElementById("message");

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const email = document.getElementById("email").value.trim();
  const password = document.getElementById("password").value;

  // Reset message
  messageEl.textContent = "";
  messageEl.className = "message";

  if (!email || !password) {
    showError("Merci de remplir l'email et le mot de passe.");
    return;
  }

  try {
    showInfo("Connexion en cours...");

    const response = await fetch(`${API_BASE_URL}/login/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        email: email,
        senha: password // ou senha_hash selon ce que tu fais côté Django
      })
    });

    if (!response.ok) {
      // on lit le message renvoyé par l'API si présent
      let errorText = "Email ou mot de passe incorrect.";
      try {
        const errorData = await response.json();
        if (errorData && errorData.detail) {
          errorText = errorData.detail;
        }
      } catch (_) {}
      showError(errorText);
      return;
    }

    const data = await response.json();

    // Exemple : on stocke l'utilisateur dans le localStorage
    localStorage.setItem("user", JSON.stringify(data));

    showSuccess("Connexion réussie ! Redirection...");

    setTimeout(() => {
        window.location.href = "dashboard.html";
    }, 700);
  } catch (error) {
    console.error(error);
    showError("Erreur réseau. Vérifie ta connexion ou réessaie plus tard.");
  }
});

function showError(text) {
  messageEl.textContent = text;
  messageEl.className = "message message--error";
}

function showSuccess(text) {
  messageEl.textContent = text;
  messageEl.className = "message message--success";
}

function showInfo(text) {
  messageEl.textContent = text;
  messageEl.className = "message";
}
