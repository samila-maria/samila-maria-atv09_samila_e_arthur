document.addEventListener("DOMContentLoaded", function () {
    var img = document.querySelector(".foto-dogs");
    if (!img) {
        return;
    }

    var pasta = "/static/portal/img/";
    var dogs = [pasta + "dog1.jpg", pasta + "dog2.jpg", pasta + "dog3.jpg"];
    var indice = 0;

    img.addEventListener("click", function () {
        indice = (indice + 1) % dogs.length;
        img.src = dogs[indice];
    });
});
