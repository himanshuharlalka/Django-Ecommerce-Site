var updateBtns = document.getElementsByClassName("update-cart");
var favBtns = document.getElementsByClassName("update-fav");
var cancelBtns = document.getElementsByClassName("cancel-order");

for (i = 0; i < favBtns.length; i++) {
  favBtns[i].addEventListener("click", function () {
    var productId = this.dataset.product;
    var action = this.dataset.action;
    console.log("productId:", productId, "Action:", action);
    console.log("USER:", user);
    updateFav(productId, action);
  });
}

for (i = 0; i < cancelBtns.length; i++) {
  cancelBtns[i].addEventListener("click", function () {
    var orderId = this.dataset.order;
    var action = this.dataset.action;
    console.log("orderId:", orderId, "Action:", action);
    console.log("USER:", user);
    cancelOrder(orderId, action);
  });
}

for (i = 0; i < updateBtns.length; i++) {
  updateBtns[i].addEventListener("click", function () {
    var productId = this.dataset.product;
    var action = this.dataset.action;
    console.log("productId:", productId, "Action:", action);
    console.log("USER:", user);

    if (user == "AnonymousUser") {
      console.log("User is not authenticated");
    } else {
      updateUserOrder(productId, action);
    }
  });
}

function updateUserOrder(productId, action) {
  console.log("User is authenticated, sending data...");

  var url = "/update_item/";

  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ productId: productId, action: action }),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      location.reload();
    });
}

function updateFav(productId, action) {
  console.log("User is authenticated, sending data...");

  var url = "/update_fav/";

  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ productId: productId, action: action }),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      location.reload();
    });
}

function cancelOrder(orderId, action) {
  console.log("User is authenticated, sending data...");

  var url = "/cancel_order/";

  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ orderId: orderId, action: action }),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      location.reload();
    });
}
function toastFav() {
  var x = document.getElementById("snackbar-fav");
  x.className = "show";
  setTimeout(function () {
    x.className = x.className.replace("show", "");
  }, 15000);
}

function toastCart() {
  var x = document.getElementById("snackbar-cart");
  x.className = "show";
  setTimeout(function () {
    x.className = x.className.replace("show", "");
  }, 15000);
}

function setStarValue(x) {
  const stars = document.getElementById("stars");
  stars.value = x;
  console.log(stars.value);
}
