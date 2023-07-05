let words = ["create", "build", "design"];
let index = 0;

function change_word() {
    let element = document.getElementById("changingWord");

    // Animate up and out
    gsap.to(element, {
        duration: 0.5,
        y: -30,
        opacity: 0,
        onComplete: () => {
            // Change the word
            element.innerHTML = words[index];
            index = (index + 1) % words.length;

            // Reset position below
            gsap.set(element, {
                y: 30,
                opacity: 0,
            });

            // Animate up and in
            gsap.to(element, {
                duration: 0.5,
                y: 0,
                opacity: 1,
            });
        }
    });
}

setInterval(change_word, 2000);