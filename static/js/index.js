$("#namer input").on("change keyup paste", function() {
    var inputValue = $(this).val();
  
    if (inputValue) {
      $(".namer-controls").addClass("active");
      $("#namer").addClass("active");
    } else {
      $(".namer-controls").removeClass("active");
      $("#namer").removeClass("active");
    }
  });
  
  $(document).on("click", ".namer-controls.active span", function() {
    if ($(this).hasClass("active")) {
      $(".namer-controls span").removeClass("active");
      $("#namer-input input").addClass("shake");
      setTimeout(function() {
        $("#namer-input input").removeClass("shake");
      }, 400);
      $("#namer-input").removeClass();
    } else {
      $(".namer-controls span").removeClass("active");
      $(this).addClass("active");
      var styleClass = $(this).text();
  
      $("#namer-input input").addClass("shake");
      setTimeout(function() {
        $("#namer-input input").removeClass("shake");
      }, 400);
  
      $("#namer-input").removeClass();
      $("#namer-input").addClass(styleClass);
    }
  });
  
  $(document).ready(function() {
    $("#namer-input input").focus();
});