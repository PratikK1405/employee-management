function validateForm(form) {
    var isValid = true;
    var inputs = form.getElementsByTagName('input');
    for (var i = 0; i < inputs.length; i++) {
        if (inputs[i].hasAttribute('required') && !inputs[i].value.trim()) {
            inputs[i].classList.add('error');
            inputs[i].placeholder = inputs[i].name.charAt(0).toUpperCase() + inputs[i].name.slice(1) + " is required";
            isValid = false;
        } else {
            inputs[i].classList.remove('error');
            inputs[i].placeholder = '';
        }
    }
    return isValid;
}

function openUpdateModal(id) {
    var modal = document.getElementById('updateModal');
    var form = document.getElementById('updateForm');
    form.action = '/update/' + id;
    modal.style.display = "block";
}

function openDeleteModal(id) {
    var modal = document.getElementById('deleteModal');
    var form = document.getElementById('deleteForm');
    form.action = '/delete/' + id;
    modal.style.display = "block";
}

function closeModal(modalId) {
    var modal = document.getElementById(modalId);
    modal.style.display = "none";
}

window.onclick = function(event) {
    var updateModal = document.getElementById('updateModal');
    var deleteModal = document.getElementById('deleteModal');
    if (event.target == updateModal) {
        updateModal.style.display = "none";
    }
    if (event.target == deleteModal) {
        deleteModal.style.display = "none";
    }
}