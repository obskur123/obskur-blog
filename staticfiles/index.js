async function typeWriter(str, el, speed) {
    for (let i = 0; i < str.length; i++) {
        await (new Promise((resolve) => setTimeout(() => resolve(el.textContent += str.charAt(i)), speed)))
    }
}

document.addEventListener('DOMContentLoaded', async () => {

    const homeTitle = document.getElementById('home-title');
    const homeDes = document.getElementById('home-description');
    const particlejs = document.getElementById('particles-js');

    if (homeTitle && homeDes) {
        await typeWriter('soy tomas', homeTitle, 100);
        await typeWriter('analista universitario en sistemas y desarrollador fullstack', homeDes, 50);
    }
    if (particlejs) {
        particlesJS.load('particles-js', 'particles.json', function () {
            console.log('callback - particles.js config loaded');
        });
    }
});