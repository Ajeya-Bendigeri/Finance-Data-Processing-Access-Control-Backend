const BASE_URL = "http://127.0.0.1:5000";

function saveAuth(token, role) {
    localStorage.setItem("token", token);
    localStorage.setItem("role", role);
}

function getToken() {
    return localStorage.getItem("token");
}

function parseJwt(token) {
    try {
        return JSON.parse(atob(token.split('.')[1]));
    } catch (e) {
        return null;
    }
}


function togglePassword(id) {
    const input = document.getElementById(id);
    input.type = input.type === "password" ? "text" : "password";
}


async function register() {
    const name = document.getElementById("name").value;
    const email = document.getElementById("reg_email").value;
    const password = document.getElementById("reg_password").value;
    const role = document.getElementById("role").value;

    if (!name || !email || !password) {
        alert("Please fill all fields");
        return;
    }

    try {
        const res = await fetch(`${BASE_URL}/api/auth/register`, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({ name, email, password, role })
        });

        const data = await res.json();

        if (res.ok) {
            alert("✅ " + data.message);
            window.location.href = "login.html";
        } else {
            alert("❌ " + (data.error || data.message));
        }

    } catch (err) {
        console.error(err);
        alert("Server error");
    }
}


async function login() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    if (!email || !password) {
        alert("Enter email & password");
        return;
    }

    try {
        const res = await fetch(`${BASE_URL}/api/auth/login`, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({ email, password })
        });

        const data = await res.json();

        if (res.ok) {
            const decoded = parseJwt(data.access_token);
            saveAuth(data.access_token, decoded.role);

            alert("✅ Login successful");
            window.location.href = "dashboard.html";
        } else {
            alert("❌ " + (data.error || data.message));
        }

    } catch (err) {
        console.error(err);
        alert("Server error");
    }
}


function logout() {
    localStorage.clear();
    alert("Logged out");
    window.location.href = "login.html";
}


window.onload = function () {
    const role = localStorage.getItem("role");
    const token = getToken();

    if (window.location.pathname.includes("dashboard.html") && !token) {
        window.location.href = "login.html";
        return;
    }

    if (document.getElementById("roleDisplay")) {
        document.getElementById("roleDisplay").innerText = "Role: " + role;

        if (role === "viewer") {
            document.getElementById("recordSection").style.display = "none";
        }
    }
};


async function getSummary() {
    try {
        const res = await fetch(`${BASE_URL}/api/dashboard/summary`, {
            headers: { "Authorization": "Bearer " + getToken() }
        });

        const data = await res.json();

        document.getElementById("summary").innerHTML =
            `Income: ${data.income}, Expense: ${data.expense}, Balance: ${data.balance}`;

    } catch (err) {
        alert("Failed to load summary");
    }
}


async function createRecord() {
    const title = document.getElementById("title").value;
    const amount = document.getElementById("amount").value;
    const category = document.getElementById("category").value;
    const date = document.getElementById("date").value;
    const type = document.getElementById("type").value;

    try {
        const res = await fetch(`${BASE_URL}/api/records/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": "Bearer " + getToken()
            },
            body: JSON.stringify({
                title,
                amount: parseFloat(amount),
                category,
                date,
                type
            })
        });

        const data = await res.json();
        alert(data.message);

    } catch (err) {
        alert("Failed to create record");
    }
}

async function getRecords() {
    try {
        const res = await fetch(`${BASE_URL}/api/records/`, {
            headers: { "Authorization": "Bearer " + getToken() }
        });

        const data = await res.json();

        const list = document.getElementById("records");
        list.innerHTML = "";

        data.data.forEach(r => {
            const li = document.createElement("li");
            li.innerText = `${r.title} - ${r.amount}`;
            list.appendChild(li);
        });

    } catch (err) {
        alert("Failed to load records");
    }
}