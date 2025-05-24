document.addEventListener('DOMContentLoaded', function () {
    const genericModal = document.getElementById('genericModal');
    let modalForm = document.getElementById('modalForm'); // Use let to allow reassignment

    // Load modal content dynamically when modal is about to show
    genericModal.addEventListener('show.bs.modal', function (event) {
        const button = event.relatedTarget;
        const url = button.getAttribute('data-url'); // URL to fetch the form content
        const title = button.getAttribute('data-title'); // Modal title

        // Set the modal title
        genericModal.querySelector('.modal-title').textContent = title;

        // Add modal=true to the URL (for both GET and POST requests)
        const actionUrl = url.includes('?') ? `${url}&modal=true` : `${url}?modal=true`;

        // Load the form into the modal body
        fetch(actionUrl)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.text();
            })
            .then(html => {
                modalForm.innerHTML = html; // Populate modal form content
                modalForm = document.getElementById('modalForm'); // Refresh reference

                // Dynamically set the action URL for the form
                modalForm.setAttribute('action', actionUrl); // Set the action attribute dynamically
            })
            .catch(error => {
                modalForm.innerHTML = `<p class="text-danger">Error loading content: ${error.message}</p>`;
            });
    });

    // Handle modal form submission
    genericModal.addEventListener('submit', function (event) {
        event.preventDefault();

        const formData = new FormData(modalForm);
        const actionUrl = modalForm.getAttribute('action');

        if (!actionUrl) {
            console.error('Form action attribute is missing. Unable to submit form.');
            modalForm.innerHTML = `<p class="text-danger">Form submission failed: missing action URL.</p>`;
            return;
        }

        fetch(actionUrl, {
            method: 'POST',
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
            },
            body: formData,
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.text(); // Check text first before parsing JSON
            })
            .then(text => {
                try {
                    const data = JSON.parse(text); // Manually parse JSON
                    if (data.success) {
                        // Close the modal if the form was successfully submitted
                        const modalInstance = bootstrap.Modal.getInstance(genericModal);
                        modalInstance.hide();

                        // Optionally update the page or show a success message
                        console.log('Modal form submitted successfully.');
                    } else {
                        // Replace modal content with form containing validation errors
                        modalForm.innerHTML = data.form_html;
                    }
                } catch (error) {
                    console.error('Error parsing JSON:', error);
                    modalForm.innerHTML = `<p class="text-danger">Error parsing response: ${error.message}</p>`;
                }
            })
            .catch(error => {
                console.error('Error submitting form:', error);
                modalForm.innerHTML = `<p class="text-danger">An error occurred while submitting the form: ${error.message}</p>`;
            });
    });

    // Clear modal content on close
    genericModal.addEventListener('hidden.bs.modal', function () {
        modalForm.innerHTML = ''; // Clear modal form content
    });
});
