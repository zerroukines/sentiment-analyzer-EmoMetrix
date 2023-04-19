let login = document.querySelector('.login');
let create = document.querySelector('.create');
let container = document.querySelector('.cntainer');

login.onclick = function () {
    container.classList.add('signinForm');
}

create.onclick = function () {
    container.classList.remove('signinForm');
}