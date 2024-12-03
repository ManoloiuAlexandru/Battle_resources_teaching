function disable_all() {
          var x = document.getElementById("reset_button");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
  var x = document.getElementById("hide_button");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
        }

function adjustFontSizeLibrary() {
  // Simple linear scaling here, but you could use more sophisticated algorithms if needed

  var list = document.getElementsByClassName("description_in_library"); //.item.style.fontSize =`${fontSize}px`;
  for (var i = 0; i < list.length; i++) {
    if (list[i].textContent !== "") {
      let fontSize = Math.floor(12 - list[i].textContent.length / 30);
      console.log(fontSize)
      list[i].style.fontSize = `${fontSize}px`;
    }
  }
}

// Function to get the text within the button and apply adjustment
// Initial call to setup on page load or when button content changes

document.addEventListener("DOMContentLoaded", function () {
  adjustFontSizeLibrary();
});

function adjustFontSizeCardInHand() {
  // Simple linear scaling here, but you could use more sophisticated algorithms if needed

  var list = document.getElementsByClassName("description"); //.item.style.fontSize =`${fontSize}px`;
  for (var i = 0; i < list.length; i++) {
    if (list[i].textContent !== "") {
      let fontSize = Math.floor(12 - list[i].textContent.length / 20);
      console.log(fontSize)
      list[i].style.fontSize = `${fontSize}px`;
    }
  }
}

// Function to get the text within the button and apply adjustment
// Initial call to setup on page load or when button content changes

document.addEventListener("DOMContentLoaded", function () {
  adjustFontSizeCardInHand();
});