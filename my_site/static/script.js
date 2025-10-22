
// Перемикання теми
const themeToggle = document.getElementById("themeToggle");
themeToggle?.addEventListener("click", () => {
  document.body.classList.toggle("dark");
  localStorage.setItem("theme", document.body.classList.contains("dark") ? "dark" : "light");
});
if (localStorage.getItem("theme") === "dark") {
  document.body.classList.add("dark");
}

// Перемикання мови
const langToggle = document.getElementById("langToggle");
if (langToggle) {
  langToggle.addEventListener("click", () => {
    const lang = langToggle.innerText === "EN" ? "UA" : "EN";
    langToggle.innerText = lang === "EN" ? "UA" : "EN";
    translatePage(lang);
  });
}

function translatePage(lang) {
  const dict = {
    EN: {
      "Новини": "News",
      "Директор: Іван Петренко | Адреса: м. Київ, вул. Свободи, 12":
        "Director: Ivan Petrenko | Address: Kyiv, Svobody St, 12"
    },
    UA: {
      "News": "Новини",
      "Director: Ivan Petrenko | Address: Kyiv, Svobody St, 12":
        "Директор: Іван Петренко | Адреса: м. Київ, вул. Свободи, 12"
    }
  };
  for (const [ua, en] of Object.entries(dict[lang])) {
    document.body.innerHTML = document.body.innerHTML.replaceAll(ua, en);
  }
}
