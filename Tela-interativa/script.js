  let card = document.querySelector(".card");
        let loginButton = document.querySelector(".loginButton");
        let cadastroButton = document.querySelector9(".cadasatroButton");

        loginButton.onclick = () => {
            card.classList.remove("cadastroActive")
            card.classList.add("loginActive")
            
        }