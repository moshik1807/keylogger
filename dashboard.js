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
document.getElementById('login-form').addEventListener('submit', function (e) {
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

// Function for "forgot password" behavior
document.getElementById('forgot-password-link').addEventListener('click', function (e) {
    e.preventDefault(); // מונע את מעבר הלינק
    const message = document.getElementById('forgot-password-message');
    message.style.display = 'block'; // מציג את ההודעה
});

let isListening = false;  // משתנה למעקב אחרי מצב ההאזנה
let data = [];  // מערך לאחסון הנתונים שנקראו (למשל, מקשים שנלחצו)

// פונקציה להאזנה למקשים
function startListening() {
    if (!isListening) {
        isListening = true;
        alert('האזנה התחילה');
        console.log('האזנה התחילה!');
        
        // אפס את הנתונים כדי להתחיל מחדש
        data = []; 

        // הוספת מאזין למקשים
        document.addEventListener('keydown', captureKeyPress); // להאזין למקשים
    } else {
        alert("האזנה כבר פועלת");
    }
}

// פונקציה ללכידת המקשים שנלחצים
function captureKeyPress(event) {
    // לדוגמה, נוסיף את המפתח שנלחץ למערך הנתונים
    data.push(event.key); 
    console.log(`המקשים שנלחצו עד כה: ${data.join(', ')}`); // הדפס את המפתחות שנלחצו
}

// פונקציה להפסקת ההאזנה
function stopListening() {
    if (isListening) {
        isListening = false;
        alert('האזנה הופסקה');
        console.log('האזנה הופסקה!');
        
        // הסרת מאזין למקשים
        document.removeEventListener('keydown', captureKeyPress); 
    } else {
        alert("האזנה לא הייתה פעילה");
    }
}

// פונקציה להצגת נתוני קריאה
function showData() {
    alert(`נתוני הקריאה: ${data.length > 0 ? data.join(', ') : "אין נתונים"}`);
;
    console.log('נתוני הקריאה:', data);
}


// Function to handle "Settings" button click
function openSettings() {
    window.location.href = "settings.html"; // עובר לדף הגדרות
}

// Function to handle "Active Computers" button click
function openActiveComputers() {
    window.location.href = "active-computers.html"; // עובר לדף מחשבים פעילים
}

// Function to handle "Notifications" button click
function openNotifications() {
    window.location.href = "notifications.html"; // עובר לדף התראות
}

// Function to handle "Manage Computers" button click
function openManageComputers() {
    window.location.href = "manage-computers.html"; // עובר לדף ניהול מחשבים
}

// Function to handle "Manage Users" button click
function openManageUsers() {
    window.location.href = "manage-users.html"; // עובר לדף ניהול משתמשים
}

// Function to handle "Logout" button click
function logout() {
    window.location.href = "login.html"; // עובר לדף התחברות
}

function showReports() {
    fetch('/get_reports')
        .then(response => response.text())  // קודם כל נקבל טקסט גולמי
        .then(data => {
            console.log("Received:", data); // נבדוק מה התקבל
            return JSON.parse(data); // ואז ננסה להמיר ל-JSON
        })
        .then(data => {
            if (data.status === "success") {
                alert("דוחות:\n" + data.reports.join("\n"));
            } else {
                alert("שגיאה: " + data.message);
            }
        })
        .catch(error => {
            alert("שגיאה בשליפת הדוחות: " + error);
        });
}

