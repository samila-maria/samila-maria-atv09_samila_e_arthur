document.addEventListener("DOMContentLoaded", function () {
    var img = document.querySelector(".foto-dogs");
    if (!img) {
        return;
    }

    var dogs = [
        "/static/portal/img/dog1.jpg",
        "/static/portal/img/dog2.jpg",
        "/static/portal/img/dog3.jpg",
    ];
    var indice = 0;

    img.addEventListener("click", function () {
        indice = (indice + 1) % dogs.length;
        img.src = dogs[indice];
    });
});
