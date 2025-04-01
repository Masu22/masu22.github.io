document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll(".dynamic-title").forEach(el => {
        const title = el.getAttribute("data-title"); // 見出しのテキスト
        const beforeColor = el.getAttribute("data-before-color") || "black"; // ::before の文字色
        const beforeBg = el.getAttribute("data-before-bg") || "gray"; // ::before の背景色

        el.textContent = title; // 見出しの内容を設定
        el.style.setProperty("--before-color", beforeColor); // CSS変数を適用
        el.style.setProperty("--before-bg", beforeBg);
    });
});
