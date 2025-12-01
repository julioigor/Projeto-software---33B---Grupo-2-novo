// dashboard.js

const API_BASE_URL = "http://localhost:8000/";

const userNameEl = document.getElementById("user-name");
const userInfoEl = document.getElementById("user-info");
const companyInfoEl = document.getElementById("company-info");
const logoutBtn = document.getElementById("logout-btn");

// 1. Vérifier que l'utilisateur est "auth"
const rawUser = localStorage.getItem("user");

if (!rawUser) {
  // Pas connecté → on renvoie vers la page de login
  window.location.href = "index.html";
} else {
  let user;
  try {
    user = JSON.parse(rawUser);
  } catch (e) {
    console.error("Impossible de parser le user :", e);
    localStorage.removeItem("user");
    window.location.href = "index.html";
  }

  if (user) {
    afficherInfosUser(user);
    chargerCompanhia(user);
    chargerProblemas(user);
  }
}

// 2. Afficher les infos de l'utilisateur
function afficherInfosUser(user) {
  userNameEl.textContent = user.nome || "Utilisateur";

  userInfoEl.textContent = `Connecté avec l'adresse ${user.email}${
    user.cargo ? " (" + user.cargo + ")" : ""
  }.`;
}

// 3. Aller chercher la companhia (ville/entreprise) associée
async function chargerCompanhia(user) {
  if (!user.companhia_id) {
    companyInfoEl.textContent =
      "Aucune ville/entreprise associée à ce compte.";
    return;
  }

  try {
    const response = await fetch(
      `${API_BASE_URL}/companhias/${user.companhia_id}/`
    );

    if (!response.ok) {
      companyInfoEl.textContent =
        "Impossible de charger les informations de la ville/entreprise.";
      return;
    }

    const companhia = await response.json();
    companyInfoEl.textContent = `${companhia.nome} – ${companhia.endereco || "Adresse non renseignée"}`;
  } catch (error) {
    console.error(error);
    companyInfoEl.textContent =
      "Erreur réseau lors du chargement de la ville/entreprise.";
  }
}

// 4. Déconnexion
logoutBtn.addEventListener("click", () => {
  localStorage.removeItem("user");
  window.location.href = "index.html";
});

function escapeHtml(str) {
    if (!str) return "";
    return str
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
}
  
async function chargerProblemas(user) {
    const listEl = document.getElementById("problems-list");
    if (!listEl) return;
  
    listEl.innerHTML = "<li>Chargement des problèmes...</li>";
  
    let url = `${API_BASE_URL}/problemas/listar/`;
    if (user.companhia_id) {
      url += `?companhia_id=${encodeURIComponent(user.companhia_id)}`;
    }
  
    try {
      const response = await fetch(url);
  
      if (!response.ok) {
        listEl.innerHTML =
          "<li>Impossible de charger les problèmes (erreur serveur).</li>";
        return;
      }
  
      const problemas = await response.json();
  
      if (!Array.isArray(problemas) || problemas.length === 0) {
        listEl.innerHTML = "<li>Aucun problème signalé pour le moment.</li>";
        return;
      }
  
      listEl.innerHTML = problemas
        .map((p) => {
          const titre = escapeHtml(p.titulo || "Sans titre");
          const status = escapeHtml(p.status || "non renseigné");
          const priorite = escapeHtml(p.prioridade || "non renseignée");
  
          return `
            <li>
              <div class="problem-title">${titre}</div>
              <div class="problem-meta">
                Statut : ${status} · Priorité : ${priorite}
              </div>
              <a href="editar-problema.html?id=${encodeURIComponent(p.id)}">Editar</a>
            </li>
          `;
        })
        .join("");
    } catch (error) {
      console.error(error);
      listEl.innerHTML =
        "<li>Erreur réseau lors du chargement des problèmes.</li>";
    }
}
  