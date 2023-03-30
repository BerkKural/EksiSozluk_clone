const likeButton = document.querySelector(".like");
const dislikeButton = document.querySelector(".dislike");
const likeCount = document.querySelector(".like .count");
const dislikeCount = document.querySelector(".dislike .count");

// Sayfa yüklendiğinde, kaydedilmiş değerleri yükle
window.addEventListener("load", () => {
  const savedLikeCount = localStorage.getItem("likeCount");
  const savedDislikeCount = localStorage.getItem("dislikeCount");
  const savedLikeColor = localStorage.getItem("likeColor");
  const savedDislikeColor = localStorage.getItem("dislikeColor");

  if (savedLikeCount) {
    likeCount.textContent = Math.min(parseInt(savedLikeCount), 1);
  }
  if (savedDislikeCount) {
    dislikeCount.textContent = Math.min(parseInt(savedDislikeCount), 1);
  }
  if (savedLikeColor) {
    likeButton.style.color = savedLikeColor;
  }
  if (savedDislikeColor) {
    dislikeButton.style.color = savedDislikeColor;
  }
});

likeButton.addEventListener("click", () => {
  if (parseInt(likeCount.textContent) < 1) {
    likeCount.textContent = parseInt(likeCount.textContent) + 1;
    localStorage.setItem("likeCount", likeCount.textContent);
    localStorage.setItem("likeColor", "green");
  }
  if (parseInt(dislikeCount.textContent) > 0) {
    dislikeCount.textContent = parseInt(dislikeCount.textContent) - 1;
    localStorage.setItem("dislikeCount", dislikeCount.textContent);
    localStorage.setItem("dislikeColor", "");
  }
  likeButton.style.color = "green";
  dislikeButton.style.backgroundColor = "";
  dislikeButton.style.color ='black'
  dislikeButton.disabled = true;
  likeButton.disabled = false;
});

dislikeButton.addEventListener("click", () => {
  if (parseInt(dislikeCount.textContent) < 1) {
    dislikeCount.textContent = parseInt(dislikeCount.textContent) + 1;
    localStorage.setItem("dislikeCount", dislikeCount.textContent);
    localStorage.setItem("dislikeColor", "red");
  }
  if (parseInt(likeCount.textContent) > 0) {
    likeCount.textContent = parseInt(likeCount.textContent) - 1;
    localStorage.setItem("likeCount", likeCount.textContent);
    localStorage.setItem("likeColor", "");
  }
  dislikeButton.style.color = "red";
  likeButton.style.backgroundColor = "";
  likeButton.disabled = true;
  likeButton.style.color ='black'
  dislikeButton.disabled = false;
});



function kaydet() {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;
  const email = document.getElementById("email").value;
  const user = {
    username: username,
    password: password,
    email: email
  };

  let users = JSON.parse(localStorage.getItem("users")) || [];
  users.push(user);
  localStorage.setItem("users", JSON.stringify(users));
  document.getElementById("alert").innerHTML = "Kullanıcı adı ve şifre kaydedildi! Giriş Sayfasına yönlendiriliyorsunuz!";
  setTimeout(function() {
    window.location.href = "login.html";
  }, 3000);
}

function getUsers() {
  return JSON.parse(localStorage.getItem("users")) || [];
}

function showUsers() {
  const users = getUsers();
  let html = "";
  for (let i = 0; i < users.length; i++) {
    html += `
      <tr>
        <td>${users[i].username}</td>
        <td>${users[i].email}</td>
        <td><button onclick="deleteUser(${i})">Sil</button></td>
      </tr>
    `;
  }
  document.getElementById("user-list").innerHTML = html;
}

function deleteUser(index) {
  const users = getUsers();
  users.splice(index, 1);
  localStorage.setItem("users", JSON.stringify(users));
  showUsers();
}
showUsers();


function giris() {
  const users = getUsers();
  let email = document.getElementById("email").value;
  let password = document.getElementById("password").value;
  let girisOnay = document.getElementById("giris_onay");

  for (let i = 0; i < users.length; i++) {
    if (email == users[i].email && password == users[i].password) {
      girisOnay.innerHTML = "Giriş başarılı! Anasayfaya yönlendiriliyorsunuz";
      setTimeout(function() {
        window.location.href = "index.html";
      }, 3000);
      return;
    }
  }

  girisOnay.innerHTML = "Giriş başarısız!";
}

