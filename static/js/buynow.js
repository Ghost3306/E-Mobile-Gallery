function validatePhone(input) {
    input.value = input.value.replace(/\D/g, '');
    if (input.value.length > 10) {
      input.value = input.value.slice(0, 10);
    }

}

function validatePincode(input) {
    input.value = input.value.replace(/\D/g, '');
    if (input.value.length > 10) {
      input.value = input.value.slice(0, 10);
    }

}


$(document).ready(function() {
    $('#addressForm').on('submit', function(e) {
      e.preventDefault(); // Prevent the default form submission
      var formData = $(this).serialize(); // Serialize form data

      $.ajax({
        type: 'POST',
        url: '', // Use the current URL
        data: formData,
        success: function(response) {
          $('#responseMessage').html('<div class="alert alert-success">Form submitted successfully!</div>');
        },
        error: function(response) {
          $('#responseMessage').html('<div class="alert alert-danger">An error occurred. Please try again.</div>');
        }
      });
    });
  });