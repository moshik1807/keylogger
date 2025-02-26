// Function to toggle language menu visibility
function toggleLanguageMenu() {
  const menu = document.getElementById("language-menu");
  menu.style.display = menu.style.display === "none" ? "block" : "none";
}

// Function to toggle the "about us" section
function toggleAboutUs() {
  window.location.href = "about-us.html"; // דף חדש על "קצת עלינו"
}

// Function to validate login
document.getElementById('login-form').addEventListener('submit', function(e) {
  e.preventDefault();
  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;

  const users = {
      "yakiruzan": "319149910",
      "moshecohen": "212311807"
  };

  const errorMessage = document.querySelector('.error-message'); // אגרום שהודעת השגיאה תהיה קבועה
  errorMessage.style.display = 'none'; // מוסר את הודעת השגיאה מהתצוגה אם אין בעיה

  if (users[username] && users[username] === password) {
      window.location.href = "dashboard.html"; // דף תוכן לאחר התחברות מוצלחת
  } else {
      errorMessage.style.display = 'block'; // אם יש שגיאה - מציג את הודעת השגיאה
  }
});

// Function to handle language selection in the menu
document.addEventListener('DOMContentLoaded', function () {
  const languageButtons = document.querySelectorAll('.language-menu button');

  languageButtons.forEach(function (button) {
    button.addEventListener('click', function () {
      const selectedLanguage = button.innerText;
      changeLanguage(selectedLanguage);
    });
  });

  // Function for "forgot password" behavior
  document.getElementById('forgot-password-link').addEventListener('click', function(e) {
    e.preventDefault(); // מונע את מעבר הלינק
    const message = document.getElementById('forgot-password-message');
    message.style.display = 'block'; // מציג את ההודעה
  });
});

// Function to send data to the server
function sendDataToServer(data) {
  fetch('http://127.0.0.1:8080/receive_data', {  // שים לב שזו הכתובת של השרת המקומי שלך
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
  .then(response => response.json())
  .then(responseData => {
    console.log('Data sent successfully:', responseData);
  })
  .catch(error => {
    console.error('Error sending data:', error);
  });
}

// דוגמת שליחת נתונים מוצפנים
const exampleData = {
  data: "some encrypted data",  // תעביר כאן את הנתונים המוצפנים שלך
  machine_name: "Machine_1"
};

// שליחה של נתונים לשרת
sendDataToServer(exampleData);
