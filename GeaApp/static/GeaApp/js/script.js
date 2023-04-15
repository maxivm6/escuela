(function () {

    var blur = document.querySelector('.blur');
    var popup = document.querySelector('.form-popup');
    var openForm = document.querySelector('.nav-link.link3');
    var close = document.querySelector('.close');
    var form = document.querySelector('.form-popup form');
    var nameInput = form.querySelector('input[name="name"]');
    var emailInput = form.querySelector('input[name="email"]');
    var btnSubmit = form.querySelector('.btn-submit');


    openForm.addEventListener('click',function() {
        console.log('La función openFormPopup() se está llamando correctamente');
        blur.style.display = 'block';
        popup.classList.add('show');
    });

    close.addEventListener('click', function () {
        blur.style.display = 'none';
        popup.classList.remove('show');
    });

    function validateForm() {
        if (nameInput.value.trim() === '') {
            nameInput.classList.add('invalid');
            nameError.innerHTML = 'Por favor, ingresa tu nombre.';
            return false;
        }
        if (!/\S+@\S+\.\S+/.test(emailInput.value)) {
            alert('Por favor, ingresa una dirección de correo electrónico válida.');
            return false;
        }
        return true;
    }

    btnSubmit.addEventListener('click', function (e) {
        e.preventDefault();
        if (validateForm()) {
            // Envía el formulario
            form.submit();
        }
    });




})();