document.addEventListener("DOMContentLoaded", function() {
    const menuButton = document.getElementById("menu-button");
    const sideMenu = document.getElementById("side-menu");
    const closeButton = document.getElementById("close-button");

    // メニューを開く
    menuButton.addEventListener("click", function() {
        sideMenu.classList.add("open");
    });

    // メニューを閉じる
    closeButton.addEventListener("click", function() {
        sideMenu.classList.remove("open");
    });

    // メニューの外側をクリックしたら閉じる
    document.addEventListener("click", function(event) {
        if (!sideMenu.contains(event.target) && event.target !== menuButton) {
            sideMenu.classList.remove("open");
        }
    });
});
