document.addEventListener("DOMContentLoaded", function() {
    const footerMenu = document.getElementById("footer-menu");
    let lastScrollTop = 0;

    window.addEventListener("scroll", function() {
        let scrollTop = window.scrollY || document.documentElement.scrollTop;

        if (scrollTop > 50) { // 50px以上スクロールしたら表示
            footerMenu.classList.add("show");
        } else {
            footerMenu.classList.remove("show"); // 一番上では隠す
        }

        lastScrollTop = scrollTop;
    });
});
