  // script.js

  // Get the canvas element
  var canvas = document.getElementById("myCanvas");

  // Check if the browser supports the canvas element
  if (canvas.getContext) {
    // Get the canvas 2D context
    var ctx = canvas.getContext("2d");

    // Set the fill color
    ctx.fillStyle = "lightblue";

    // Draw a rectangle
    ctx.fillRect(10, 10, 380, 180);

    // Set the text properties
    ctx.font = "30px Arial";
    ctx.fillStyle = "black";

    // Write "Grade 3" within the canvas
    ctx.fillText("Grade 3", 50, 100);

    // Add click event listener to the canvas
    canvas.addEventListener("click", function(event) {
      // Get the mouse position relative to the canvas
      var rect = canvas.getBoundingClientRect();
      var x = event.clientX - rect.left;
      var y = event.clientY - rect.top;

      // Check if the click is within the desired area
      if (x >= 10 && x <= 390 && y >= 10 && y <= 190) {
        // Redirect to the desired link
        window.location.href = "{{ url_for('views.grade3') }}";
      }
    });
  }