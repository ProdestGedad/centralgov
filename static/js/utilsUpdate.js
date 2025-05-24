// Function to retrieve the CSRF token from the meta tag
function getCsrfToken() {
    return document.querySelector('meta[name="csrf-token"]').getAttribute('content');
}

const utilsUrl = window.location.origin + '/utils/';

function performAction(action) {
    fetch(utilsUrl, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCsrfToken(),  // Use the CSRF token retrieved from the meta tag
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                action: action
            })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (data.status === 'success') {
                alert(data.message);
            } else if (data.status === 'partial_success') {
                let message = `${data.message}\n\nDetalhes dos Erros:\n${data.errors.join('\n')}`;
                alert(message);
            } else {
                alert(`Erro: ${data.message}`);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Ocorreu um erro ao executar ' + action);
        });
}
